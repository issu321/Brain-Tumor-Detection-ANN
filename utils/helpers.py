import os
import secrets
from datetime import datetime
from flask import current_app
from PIL import Image
import random
import string

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and            filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def save_uploaded_file(file):
    """Save uploaded file with secure name"""
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(file.filename)
    filename = random_hex + f_ext
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    return filename, file_path

def generate_random_string(length=10):
    """Generate random string"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def format_datetime(dt):
    """Format datetime for display"""
    if dt:
        return dt.strftime("%B %d, %Y at %I:%M %p")
    return "N/A"

def get_time_ago(dt):
    """Get human readable time ago"""
    if not dt:
        return "N/A"

    now = datetime.utcnow()
    diff = now - dt

    seconds = diff.total_seconds()

    if seconds < 60:
        return "just now"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif seconds < 604800:
        days = int(seconds / 86400)
        return f"{days} day{'s' if days > 1 else ''} ago"
    else:
        return dt.strftime("%b %d, %Y")

def get_confidence_color(confidence):
    """Get color based on confidence score"""
    if confidence >= 90:
        return '#10b981'  # Green
    elif confidence >= 70:
        return '#f59e0b'  # Yellow/Orange
    else:
        return '#ef4444'  # Red

def get_status_badge(status):
    """Get status badge HTML"""
    colors = {
        'completed': 'success',
        'pending': 'warning',
        'processing': 'info',
        'failed': 'danger'
    }
    return colors.get(status, 'secondary')
