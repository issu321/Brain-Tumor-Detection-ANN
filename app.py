import os
import secrets
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import time

from config import Config
from models import db, User, Scan, ActivityLog, ContactMessage
from forms import RegistrationForm, LoginForm, UpdateProfileForm, ScanUploadForm, ContactForm, AdminUserCreateForm
from utils.helpers import allowed_file, save_uploaded_file

# Try to import predictor - works with or without TensorFlow
try:
    from utils.predictor import predictor
    PREDICTOR_AVAILABLE = True
except Exception as e:
    print(f"Warning: Could not load predictor: {e}")
    PREDICTOR_AVAILABLE = False

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please login to access this page.'
login_manager.login_message_category = 'warning'

# Context processor for templates
@app.context_processor
def inject_globals():
    return {
        'now': datetime.utcnow(),
        'config': app.config
    }

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ==========================================
# ROUTES
# ==========================================

@app.route('/')
def home():
    """Home page"""
    return render_template('home.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form"""
    form = ContactForm()
    if form.validate_on_submit():
        message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(message)
        db.session.commit()
        flash('Thank you! Your message has been sent successfully.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

# ==========================================
# AUTH ROUTES
# ==========================================

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            email=form.email.data,
            full_name=form.full_name.data,
            phone=form.phone.data,
            password_hash=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        activity = ActivityLog(
            user_id=user.id,
            action='User Registration',
            description=f'New user registered: {user.username}',
            ip_address=request.remote_addr
        )
        db.session.add(activity)
        db.session.commit()

        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            if not user.is_active:
                flash('Your account has been deactivated. Contact admin.', 'danger')
                return redirect(url_for('login'))

            login_user(user, remember=form.remember.data)
            user.last_login = datetime.utcnow()
            db.session.commit()

            activity = ActivityLog(
                user_id=user.id,
                action='User Login',
                description=f'User logged in from {request.remote_addr}',
                ip_address=request.remote_addr
            )
            db.session.add(activity)
            db.session.commit()

            next_page = request.args.get('next')
            flash(f'Welcome back, {user.full_name or user.username}!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    """User logout"""
    activity = ActivityLog(
        user_id=current_user.id,
        action='User Logout',
        description='User logged out',
        ip_address=request.remote_addr
    )
    db.session.add(activity)
    db.session.commit()

    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('home'))

# ==========================================
# DASHBOARD ROUTES
# ==========================================

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    scans = Scan.query.filter_by(user_id=current_user.id).order_by(Scan.scan_date.desc()).all()

    total_scans = len(scans)
    tumor_detected = sum(1 for s in scans if s.prediction == 'Tumor Detected')
    no_tumor = sum(1 for s in scans if s.prediction == 'No Tumor')

    avg_confidence = 0
    if total_scans > 0:
        avg_confidence = round(sum(s.confidence_score for s in scans) / total_scans, 1)

    chart_labels = ['No Tumor', 'Glioma', 'Meningioma', 'Pituitary']
    chart_data = [
        sum(1 for s in scans if s.tumor_type is None and s.prediction == 'No Tumor'),
        sum(1 for s in scans if s.tumor_type == 'Glioma'),
        sum(1 for s in scans if s.tumor_type == 'Meningioma'),
        sum(1 for s in scans if s.tumor_type == 'Pituitary')
    ]

    recent_scans_list = scans[:10]
    trend_labels = [s.scan_date.strftime('%b %d') for s in reversed(recent_scans_list)]
    trend_data = [round(s.confidence_score, 1) for s in reversed(recent_scans_list)]

    if not trend_labels:
        trend_labels = []
        trend_data = []

    return render_template('dashboard.html',
                         total_scans=total_scans,
                         tumor_detected=tumor_detected,
                         no_tumor=no_tumor,
                         avg_confidence=avg_confidence,
                         recent_scans=scans[:5],
                         chart_labels=chart_labels,
                         chart_data=chart_data,
                         trend_labels=trend_labels,
                         trend_data=trend_data)

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_scan():
    """Upload and analyze scan"""
    form = ScanUploadForm()

    if request.method == 'POST':
        if 'scanFile' not in request.files:
            flash('No file selected.', 'danger')
            return redirect(request.url)

        file = request.files['scanFile']
        if file.filename == '':
            flash('No file selected.', 'danger')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename, file_path = save_uploaded_file(file)
            original_filename = secure_filename(file.filename)

            # Run prediction (works with or without TensorFlow)
            if PREDICTOR_AVAILABLE:
                result = predictor.predict(file_path)
            else:
                # Fallback if predictor failed to import entirely
                from utils.predictor import BrainTumorPredictor
                temp_predictor = BrainTumorPredictor()
                result = temp_predictor.predict(file_path)

            # Save scan to database
            scan = Scan(
                user_id=current_user.id,
                filename=filename,
                original_filename=original_filename,
                file_path=file_path,
                prediction=result['prediction'],
                tumor_type=result.get('tumor_type'),
                confidence=result['confidence'],
                confidence_score=result['confidence_score'],
                processing_time=result.get('processing_time'),
                notes=form.notes.data,
                status='completed'
            )
            db.session.add(scan)
            db.session.commit()

            activity = ActivityLog(
                user_id=current_user.id,
                action='Scan Upload',
                description=f'Uploaded scan: {original_filename} - Result: {result["prediction"]}',
                ip_address=request.remote_addr
            )
            db.session.add(activity)
            db.session.commit()

            flash('Scan analyzed successfully!', 'success')
            return redirect(url_for('scan_result', scan_id=scan.id))
        else:
            flash('Invalid file type. Please upload an image file (JPG, PNG, TIFF, BMP).', 'danger')

    return render_template('upload.html', form=form)

@app.route('/result/<int:scan_id>')
@login_required
def scan_result(scan_id):
    """View scan result"""
    scan = Scan.query.get_or_404(scan_id)

    if scan.user_id != current_user.id and current_user.role != 'admin':
        abort(403)

    # Get probabilities for display
    probabilities = {
        'No Tumor': 0.25,
        'Glioma': 0.25,
        'Meningioma': 0.25,
        'Pituitary': 0.25
    }

    if scan.prediction == 'No Tumor':
        probabilities['No Tumor'] = scan.confidence
        remaining = (1 - scan.confidence) / 3
        probabilities['Glioma'] = remaining
        probabilities['Meningioma'] = remaining
        probabilities['Pituitary'] = remaining
    else:
        tumor_type = scan.tumor_type or 'Glioma'
        probabilities[tumor_type] = scan.confidence
        remaining = (1 - scan.confidence) / 3
        for key in probabilities:
            if key != tumor_type:
                probabilities[key] = remaining

    return render_template('result.html', scan=scan, probabilities=probabilities)

@app.route('/history')
@login_required
def history():
    """Scan history with pagination"""
    page = request.args.get('page', 1, type=int)
    per_page = 10

    pagination = Scan.query.filter_by(user_id=current_user.id)        .order_by(Scan.scan_date.desc())        .paginate(page=page, per_page=per_page, error_out=False)

    return render_template('history.html', scans=pagination.items, pagination=pagination)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """User profile"""
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.full_name = form.full_name.data
        current_user.phone = form.phone.data
        db.session.commit()

        activity = ActivityLog(
            user_id=current_user.id,
            action='Profile Update',
            description='User updated their profile',
            ip_address=request.remote_addr
        )
        db.session.add(activity)
        db.session.commit()

        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))

    return render_template('profile.html', form=form)

# ==========================================
# ADMIN ROUTES
# ==========================================

@app.route('/admin')
@login_required
def admin_dashboard():
    """Admin dashboard"""
    if current_user.role != 'admin':
        abort(403)

    total_users = User.query.count()
    total_scans_all = Scan.query.count()
    total_tumors = Scan.query.filter(Scan.prediction == 'Tumor Detected').count()
    total_messages = ContactMessage.query.count()

    users = User.query.order_by(User.created_at.desc()).all()
    recent_messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).limit(5).all()

    admin_chart_data = [
        Scan.query.filter(Scan.prediction == 'No Tumor').count(),
        Scan.query.filter(Scan.tumor_type == 'Glioma').count(),
        Scan.query.filter(Scan.tumor_type == 'Meningioma').count(),
        Scan.query.filter(Scan.tumor_type == 'Pituitary').count()
    ]

    create_form = AdminUserCreateForm()

    return render_template('admin.html',
                         total_users=total_users,
                         total_scans_all=total_scans_all,
                         total_tumors=total_tumors,
                         total_messages=total_messages,
                         users=users,
                         recent_messages=recent_messages,
                         admin_chart_data=admin_chart_data,
                         create_form=create_form)

@app.route('/admin/create-user', methods=['POST'])
@login_required
def admin_create_user():
    """Admin create user"""
    if current_user.role != 'admin':
        abort(403)

    form = AdminUserCreateForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            email=form.email.data,
            full_name=form.full_name.data,
            phone=form.phone.data,
            password_hash=hashed_password,
            role=form.role.data
        )
        db.session.add(user)
        db.session.commit()
        flash(f'User {user.username} created successfully!', 'success')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'danger')

    return redirect(url_for('admin_dashboard'))

# ==========================================
# ERROR HANDLERS
# ==========================================

@app.errorhandler(404)
def error_404(error):
    return render_template('error.html', error_code=404, error_title='Page Not Found',
                         error_message='The page you are looking for does not exist.'), 404

@app.errorhandler(403)
def error_403(error):
    return render_template('error.html', error_code=403, error_title='Access Forbidden',
                         error_message='You do not have permission to access this page.'), 403

@app.errorhandler(500)
def error_500(error):
    return render_template('error.html', error_code=500, error_title='Server Error',
                         error_message='Something went wrong on our end. Please try again later.'), 500

# ==========================================
# DATABASE INIT
# ==========================================

@app.cli.command('init-db')
def init_db():
    """Initialize database with tables"""
    db.create_all()
    print('Database initialized!')

    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            email='admin@brainscan.ai',
            full_name='System Administrator',
            password_hash=generate_password_hash('admin123'),
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()
        print('Admin user created: admin / admin123')

# ==========================================
# RUN
# ==========================================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
