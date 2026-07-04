# Brain Tumor Detection Using ANN

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1+-green?style=flat&logo=flask)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.18+-orange?style=flat&logo=tensorflow)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> **AI-Powered Medical Diagnosis System** - Detect brain tumors using Artificial Neural Networks with a stunning glassmorphism UI.

## Features

- **ANN-Based Detection**: Advanced Artificial Neural Network for precise tumor classification
- **4 Tumor Types**: Detects Glioma, Meningioma, Pituitary tumors, and No Tumor
- **Glassmorphism UI**: Modern, attractive frosted glass design with animated backgrounds
- **Full Authentication**: Login, Register, Profile management with role-based access
- **Dashboard**: Interactive charts and statistics with real-time analytics
- **Scan History**: Complete history with pagination and detailed results
- **Confidence Analysis**: Visual confidence rings and probability distributions
- **Admin Panel**: User management, system overview, and contact messages
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Tech Stack

- **Backend**: Flask 3.1, SQLAlchemy, Flask-Login, Flask-WTF
- **Frontend**: HTML5, CSS3 (Glassmorphism), Bootstrap 5, Chart.js, Font Awesome
- **AI/ML**: TensorFlow 2.18+ (optional), Keras, NumPy, Pillow
- **Database**: SQLite (easily switchable to PostgreSQL/MySQL)

## Python Version Compatibility

| Python Version | TensorFlow Support | Status |
|----------------|-------------------|--------|
| 3.9 - 3.12 | ✅ Full support | Recommended |
| 3.13 | ⚠️ Partial (TF 2.20+) | Supported |
| **3.14** | ❌ **Not yet** | App works in simulation mode |

> **Note**: As of July 2026, TensorFlow does NOT support Python 3.14. The app includes a built-in simulation mode that works perfectly without TensorFlow. See [Python 3.14 Setup](#python-314-setup) below.

## Installation

### Option 1: Python 3.12 (Recommended - Full TensorFlow Support)

```bash
# Use Python 3.12
py -3.12 -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

### Option 2: Python 3.14 (Simulation Mode - No TensorFlow)

```bash
# Python 3.14 - TensorFlow not available yet
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install everything EXCEPT TensorFlow
pip install Flask==3.1.0 Flask-SQLAlchemy==3.1.1 Flask-Login==0.6.3 Flask-WTF==1.2.2 WTForms==3.2.1 Werkzeug==3.1.3 Pillow==11.1.0 numpy==2.2.0 scikit-learn==1.6.1 matplotlib==3.10.0 pandas==2.2.3 python-dotenv==1.0.1 email-validator==2.2.0
```

Or simply:
```bash
pip install -r requirements.txt
# TensorFlow will be skipped automatically (commented out in requirements.txt)
```

## Running the Application

```bash
# Initialize database (auto-creates tables + admin user)
python app.py

# Or use Flask CLI
flask init-db

# The app will be available at http://localhost:5000
```

## Default Admin Credentials

- **Username**: `admin`
- **Password**: `admin123`

> **Important**: Change the default admin password in production!

## Project Structure

```
brain_tumor_detection/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── models.py              # Database models
├── forms.py               # WTForms definitions
├── .env                   # Environment variables
├── README.md              # This file
├── static/
│   ├── css/
│   │   └── style.css      # Glassmorphism theme
│   ├── js/
│   │   └── main.js        # Frontend JavaScript
│   ├── uploads/           # Uploaded scan images
│   └── images/            # Static images
├── templates/             # Jinja2 HTML templates
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── result.html
│   ├── history.html
│   ├── profile.html
│   ├── admin.html
│   ├── about.html
│   ├── contact.html
│   └── error.html
└── utils/
    ├── predictor.py       # ANN prediction logic (TensorFlow optional)
    └── helpers.py         # Utility functions
```

## Adding Your Trained Model

To use a real trained ANN model:

1. Train your model and save it as `model.h5` or `model.keras`
2. Place it in the project root directory
3. Update `utils/predictor.py`:

```python
predictor = BrainTumorPredictor(model_path='model.h5')
predictor.load_model()
```

The model should output 4 classes: `[No Tumor, Glioma, Meningioma, Pituitary]`

## Simulation Mode (No TensorFlow)

If TensorFlow is not installed, the app automatically uses **simulation mode**:
- Generates realistic predictions based on image properties
- Provides confidence scores and probability distributions
- Perfect for development, testing, and UI demonstration
- All features work exactly the same

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/login` | GET/POST | User login |
| `/register` | GET/POST | User registration |
| `/dashboard` | GET | User dashboard |
| `/upload` | GET/POST | Upload & analyze scan |
| `/result/<id>` | GET | View scan result |
| `/history` | GET | Scan history |
| `/profile` | GET/POST | User profile |
| `/admin` | GET | Admin panel |
| `/about` | GET | About page |
| `/contact` | GET/POST | Contact page |

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key | Auto-generated |
| `DATABASE_URL` | Database connection string | `sqlite:///site.db` |
| `FLASK_ENV` | Flask environment | `development` |

## License

This project is licensed under the MIT License.

## Author

**Mohammed Usman**

- GitHub: [@issu321](https://github.com/issu321)
- Email: [jaafreeusman@gmail.com](mailto:jaafreeusman@gmail.com)
- Phone: +91 8884294749
- Repository: [Brain-Tumor-Detection-ANN](https://github.com/issu321/Brain-Tumor-Detection-ANN)

## Disclaimer

This is an AI-assisted diagnostic tool and should **NOT** replace professional medical advice. Always consult with qualified healthcare providers for medical decisions.

---

<p align="center">Made with ❤️ by Mohammed Usman</p>
