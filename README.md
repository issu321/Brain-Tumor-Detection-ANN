<div align="center">

<!-- Animated Typing Header -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=32&duration=3000&pause=1000&color=667EEA&center=true&vCenter=true&width=800&lines=🧠+Brain+Tumor+Detection;AI-Powered+Medical+Diagnosis;ANN+Classification+System" alt="Typing Header" />

<br>

<!-- Animated Shields -->
<img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white&color=3776AB" alt="Python" />
<img src="https://img.shields.io/badge/Flask-3.1+-green?style=for-the-badge&logo=flask&logoColor=white&color=000000" alt="Flask" />
<img src="https://img.shields.io/badge/TensorFlow-2.18+-orange?style=for-the-badge&logo=tensorflow&logoColor=white&color=FF6F00" alt="TensorFlow" />
<img src="https://img.shields.io/badge/SQLAlchemy-3.1+-red?style=for-the-badge&logo=sqlite&logoColor=white&color=003B57" alt="SQLAlchemy" />
<img src="https://img.shields.io/badge/Bootstrap-5+-purple?style=for-the-badge&logo=bootstrap&logoColor=white&color=7952B3" alt="Bootstrap" />
<br>
<img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=white&color=FCD34D" alt="License" />
<img src="https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge&logo=checkmarx&logoColor=white&color=10B981" alt="Status" />
<img src="https://img.shields.io/badge/UI-Glassmorphism-9cf?style=for-the-badge&logo=windowsterminal&logoColor=white&color=38BDF8" alt="UI" />

<br><br>

<!-- Neural Network Animation Banner -->
<img src="./neural_network.svg" width="100%" alt="Neural Network Architecture" />

<br>

> **🎯 AI-Powered Medical Diagnosis System** — Detect brain tumors using Artificial Neural Networks with a stunning glassmorphism UI, real-time analytics, and production-grade authentication.

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🏗️ System Architecture](#️-system-architecture)
- [📊 Data Flow](#-data-flow)
- [🗺️ User Journey](#️-user-journey)
- [🛠️ Tech Stack](#️-tech-stack)
- [💻 Installation](#-installation)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🔌 API Endpoints](#-api-endpoints)
- [🧠 Model Integration](#-model-integration)
- [🔧 Environment Variables](#-environment-variables)
- [📸 Screenshots](#-screenshots)
- [👤 Author](#-author)
- [⚖️ License](#️-license)
- [⚠️ Disclaimer](#️-disclaimer)

---

## ✨ Features

<div align="center">

| Feature | Description | Status |
|---------|-------------|--------|
| 🧠 **ANN-Based Detection** | Advanced Artificial Neural Network for precise tumor classification | ✅ Active |
| 🔬 **4 Tumor Types** | Detects Glioma, Meningioma, Pituitary tumors, and No Tumor | ✅ Active |
| 🎨 **Glassmorphism UI** | Modern frosted glass design with animated backgrounds | ✅ Active |
| 🔐 **Full Authentication** | Login, Register, Profile with role-based access control | ✅ Active |
| 📊 **Interactive Dashboard** | Real-time charts and statistics with Chart.js | ✅ Active |
| 📜 **Scan History** | Complete history with pagination and detailed results | ✅ Active |
| 🎯 **Confidence Analysis** | Visual confidence rings and probability distributions | ✅ Active |
| 🛡️ **Admin Panel** | User management, system overview, and contact messages | ✅ Active |
| 📱 **Responsive Design** | Works on desktop, tablet, and mobile devices | ✅ Active |
| 🔄 **Simulation Mode** | Works without TensorFlow for development & testing | ✅ Active |

</div>

---

## 🏗️ System Architecture

<div align="center">

<img src="./system_architecture.svg" width="100%" alt="System Architecture" />

</div>

### 🧩 Component Breakdown

```mermaid
graph TB
    subgraph "🌐 Client Layer"
        A[👤 User Browser]
        B[📱 Mobile Device]
    end

    subgraph "🎨 Presentation Layer"
        C[Glassmorphism UI]
        D[HTML5 + CSS3 + Bootstrap 5]
        E[Chart.js + Font Awesome]
    end

    subgraph "⚡ Application Layer"
        F[Flask 3.1 Backend]
        G[Flask-Login Auth]
        H[Flask-WTF Forms]
        I[SQLAlchemy ORM]
        J[Werkzeug Security]
    end

    subgraph "🧠 AI / ML Layer"
        K[TensorFlow 2.18+]
        L[Keras Model]
        M[Image Preprocessing]
        N[Simulation Mode]
    end

    subgraph "💾 Data Layer"
        O[SQLite Database]
        P[Users Table]
        Q[Scans Table]
        R[Contacts Table]
    end

    A --> C
    B --> C
    C --> D
    D --> E
    C --> F
    F --> G
    F --> H
    F --> I
    F --> J
    F --> K
    K --> L
    L --> M
    M --> N
    I --> O
    O --> P
    O --> Q
    O --> R

    style A fill:#f59e0b,stroke:#fff,stroke-width:2px,color:#fff
    style F fill:#10b981,stroke:#fff,stroke-width:2px,color:#fff
    style K fill:#8b5cf6,stroke:#fff,stroke-width:2px,color:#fff
    style O fill:#3b82f6,stroke:#fff,stroke-width:2px,color:#fff
```

---

## 📊 Data Flow

<div align="center">

<img src="./data_flow.svg" width="100%" alt="Data Flow Pipeline" />

</div>

### 🔀 Processing Pipeline (Mermaid)

```mermaid
flowchart LR
    A[📤 Upload MRI] -->|File Validation| B[🔍 Validate]
    B -->|Security Scan| C[⚙️ Preprocess]
    C -->|Resize 224x224| D[🧠 ANN Model]
    D -->|Forward Pass| E[📈 Analyze]
    E -->|Confidence Score| F[🎯 Result]
    F -->|Store Data| G[(💾 Database)]
    F -->|Render UI| H[📊 Dashboard]

    style A fill:#f97316,stroke:#fff,stroke-width:2px,color:#fff
    style B fill:#eab308,stroke:#fff,stroke-width:2px,color:#fff
    style C fill:#22c55e,stroke:#fff,stroke-width:2px,color:#fff
    style D fill:#3b82f6,stroke:#fff,stroke-width:2px,color:#fff
    style E fill:#a855f7,stroke:#fff,stroke-width:2px,color:#fff
    style F fill:#ec4899,stroke:#fff,stroke-width:2px,color:#fff
    style G fill:#3b82f6,stroke:#fff,stroke-width:2px,color:#fff
    style H fill:#8b5cf6,stroke:#fff,stroke-width:2px,color:#fff
```

---

## 🗺️ User Journey

<div align="center">

<img src="./app_workflow.svg" width="100%" alt="User Journey & Workflow" />

</div>

### 🔄 Application State Machine

```mermaid
stateDiagram-v2
    [*] --> Landing: Visit Site
    Landing --> About: Click About
    Landing --> Contact: Click Contact
    Landing --> Login: Click Login
    Landing --> Register: Click Register

    Login --> Dashboard: Auth Success
    Register --> Dashboard: Account Created

    Dashboard --> Upload: New Scan
    Dashboard --> History: View Records
    Dashboard --> Profile: Edit Account
    Dashboard --> Admin: Admin Role

    Upload --> Processing: Submit Image
    Processing --> Result: Prediction Complete
    Result --> History: Save Record
    Result --> Dashboard: Done

    History --> Result: View Details
    History --> Dashboard: Back

    Profile --> Dashboard: Save Changes
    Admin --> Dashboard: Back

    Dashboard --> Login: Logout
    Login --> [*]
    About --> [*]
    Contact --> [*]
```

---

## 🛠️ Tech Stack

<div align="center">

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| **Flask** | 3.1+ | Web framework & routing |
| **SQLAlchemy** | 3.1+ | ORM & database management |
| **Flask-Login** | 0.6.3 | Session-based authentication |
| **Flask-WTF** | 1.2.2 | Form handling & CSRF protection |
| **Werkzeug** | 3.1.3 | Password hashing & WSGI utilities |

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| **HTML5** | — | Semantic markup |
| **CSS3** | — | Glassmorphism & animations |
| **Bootstrap 5** | 5.x | Responsive grid & components |
| **Chart.js** | 4.x | Interactive data visualization |
| **Font Awesome** | 6.x | Icon library |

### AI / ML
| Technology | Version | Purpose |
|------------|---------|---------|
| **TensorFlow** | 2.18+ | Deep learning framework |
| **Keras** | 3.x | High-level neural network API |
| **NumPy** | 2.2+ | Numerical computations |
| **Pillow** | 11.1+ | Image processing |
| **scikit-learn** | 1.6+ | ML utilities & metrics |

### Database
| Technology | Version | Purpose |
|------------|---------|---------|
| **SQLite** | 3.x | Default development database |
| **PostgreSQL** | 15+ | Production database (optional) |
| **MySQL** | 8.0+ | Alternative production database |

</div>

---

## 💻 Installation

### 🐍 Python Version Compatibility

<div align="center">

| Python Version | TensorFlow Support | Status | Recommendation |
|:-------------:|:------------------:|:------:|:--------------:|
| **3.9 - 3.12** | ✅ Full Support | 🟢 Recommended | **Use this** |
| **3.13** | ⚠️ Partial (TF 2.20+) | 🟡 Supported | Use with caution |
| **3.14** | ❌ Not Yet | 🔴 Simulation Only | App works in sim mode |

</div>

> **⚠️ Note**: As of July 2026, TensorFlow does NOT support Python 3.14. The app includes a built-in **simulation mode** that works perfectly without TensorFlow.

---

### ✅ Option 1: Python 3.12 (Recommended — Full TensorFlow Support)

```bash
# Create virtual environment with Python 3.12
py -3.12 -m venv venv

# Activate (Windows)
venv\Scriptsctivate

# Activate (macOS / Linux)
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

---

### ⚠️ Option 2: Python 3.14 (Simulation Mode — No TensorFlow)

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scriptsctivate

# Activate (macOS / Linux)
source venv/bin/activate

# Install everything EXCEPT TensorFlow
pip install Flask==3.1.0 Flask-SQLAlchemy==3.1.1 Flask-Login==0.6.3     Flask-WTF==1.2.2 WTForms==3.2.1 Werkzeug==3.1.3 Pillow==11.1.0     numpy==2.2.0 scikit-learn==1.6.1 matplotlib==3.10.0 pandas==2.2.3     python-dotenv==1.0.1 email-validator==2.2.0
```

Or simply:
```bash
pip install -r requirements.txt
# TensorFlow will be skipped automatically (commented out in requirements.txt)
```

---

## 🚀 Quick Start

```bash
# Initialize database (auto-creates tables)
python app.py

# Or use Flask CLI
flask init-db

# The app will be available at
# 🌐 http://localhost:5000
```

### 📝 Getting Started

<div align="center">

| Step | Action | Description |
|:----:|--------|-------------|
| 1 | 📝 **Register** | Create your account via the Register page |
| 2 | 🔐 **Login** | Sign in with your new credentials |
| 3 | 📤 **Upload** | Go to Upload and submit an MRI scan image |
| 4 | 🎯 **Detect** | View the AI-powered tumor detection results |
| 5 | 📊 **Explore** | Check your Dashboard, History, and Profile |
| 6 | 🛡️ **Admin** | *(Admin users)* Access the Admin Panel for system management |

</div>

> **💡 Tip**: After installing the modules, simply register an account and start detecting brain tumors right away. Enjoy the full experience!

---

## 📁 Project Structure

```mermaid
graph TD
    Root["🧠 Brain Tumor Detection/"] --> App["📄 app.py<br/>Main Flask Application"]
    Root --> Config["⚙️ config.py<br/>Configuration Settings"]
    Root --> Req["📦 requirements.txt<br/>Dependencies"]
    Root --> Models["🗃️ models.py<br/>Database Models"]
    Root --> Forms["📝 forms.py<br/>WTForms Definitions"]
    Root --> Env["🔐 .env<br/>Environment Variables"]
    Root --> Utils["🛠️ utils/"]
    Root --> Static["🎨 static/"]
    Root --> Templates["📄 templates/"]

    Utils --> Predictor["🔮 predictor.py<br/>ANN Prediction Logic"]
    Utils --> Helpers["🔧 helpers.py<br/>Utility Functions"]

    Static --> CSS["💅 css/style.css<br/>Glassmorphism Theme"]
    Static --> JS["⚡ js/main.js<br/>Frontend JavaScript"]
    Static --> Uploads["📂 uploads/<br/>Uploaded Scan Images"]
    Static --> Images["🖼️ images/<br/>Static Images"]

    Templates --> Base["📄 base.html"]
    Templates --> Home["🏠 home.html"]
    Templates --> Login["🔐 login.html"]
    Templates --> Register["📝 register.html"]
    Templates --> Dashboard["📊 dashboard.html"]
    Templates --> Upload["📤 upload.html"]
    Templates --> Result["🎯 result.html"]
    Templates --> History["📜 history.html"]
    Templates --> Profile["👤 profile.html"]
    Templates --> Admin["🛡️ admin.html"]
    Templates --> About["ℹ️ about.html"]
    Templates --> Contact["📧 contact.html"]
    Templates --> Error["❌ error.html"]

    style Root fill:#0f172a,stroke:#38bdf8,stroke-width:3px,color:#fff
    style App fill:#10b981,stroke:#fff,stroke-width:2px,color:#fff
    style Utils fill:#8b5cf6,stroke:#fff,stroke-width:2px,color:#fff
    style Static fill:#ec4899,stroke:#fff,stroke-width:2px,color:#fff
    style Templates fill:#3b82f6,stroke:#fff,stroke-width:2px,color:#fff
```

---

## 🔌 API Endpoints

<div align="center">

| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|:-------------:|
| `/` | `GET` | 🏠 Home page | ❌ |
| `/login` | `GET/POST` | 🔐 User login | ❌ |
| `/register` | `GET/POST` | 📝 User registration | ❌ |
| `/dashboard` | `GET` | 📊 User dashboard | ✅ |
| `/upload` | `GET/POST` | 📤 Upload & analyze scan | ✅ |
| `/result/<id>` | `GET` | 🎯 View scan result | ✅ |
| `/history` | `GET` | 📜 Scan history | ✅ |
| `/profile` | `GET/POST` | 👤 User profile | ✅ |
| `/admin` | `GET` | 🛡️ Admin panel | ✅👑 |
| `/about` | `GET` | ℹ️ About page | ❌ |
| `/contact` | `GET/POST` | 📧 Contact page | ❌ |

</div>

---

## 🧠 Model Integration

### Adding Your Trained Model

To use a real trained ANN model:

1. **Train your model** and save it as `model.h5` or `model.keras`
2. **Place it** in the project root directory
3. **Update** `utils/predictor.py`:

```python
predictor = BrainTumorPredictor(model_path='model.h5')
predictor.load_model()
```

> **📋 Model Requirements**: The model should output **4 classes** in this order:
> ```
> [No Tumor, Glioma, Meningioma, Pituitary]
> ```

---

### 🔄 Simulation Mode (No TensorFlow)

If TensorFlow is not installed, the app automatically uses **simulation mode**:

- ✅ Generates realistic predictions based on image properties
- ✅ Provides confidence scores and probability distributions
- ✅ Perfect for development, testing, and UI demonstration
- ✅ All features work exactly the same

---

## 🔧 Environment Variables

<div align="center">

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key for sessions | Auto-generated |
| `DATABASE_URL` | Database connection string | `sqlite:///site.db` |
| `FLASK_ENV` | Flask environment mode | `development` |

</div>

Create a `.env` file in the project root:

```env
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=sqlite:///site.db
FLASK_ENV=production
```

---

## 📸 Screenshots

> *Screenshots will be added here. The app features a stunning glassmorphism design with animated backgrounds, interactive charts, and real-time confidence visualization.*

<div align="center">

| Page | Preview |
|------|---------|
| **🏠 Home** | Glassmorphism landing with animated particles |
| **📊 Dashboard** | Interactive Chart.js analytics & statistics |
| **📤 Upload** | Drag-and-drop MRI scan with live preview |
| **🎯 Result** | Confidence rings & probability distribution |
| **📜 History** | Paginated scan records with search & filter |
| **🛡️ Admin** | User management & system overview |

</div>

---

## 👤 Author

<div align="center">

**Mohammed Usman**

[![GitHub](https://img.shields.io/badge/GitHub-@issu321-181717?style=for-the-badge&logo=github)](https://github.com/issu321)
[![Email](https://img.shields.io/badge/Email-jaafreeusman@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jaafreeusman@gmail.com)

📦 **Repository**: [Brain-Tumor-Detection-ANN](https://github.com/issu321/Brain-Tumor-Detection-ANN)

</div>

---

## ⚖️ License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026 Mohammed Usman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## ⚠️ Disclaimer

> **🏥 This is an AI-assisted diagnostic tool and should NOT replace professional medical advice.** Always consult with qualified healthcare providers for medical decisions. The predictions generated by this system are for research and educational purposes only.

---

<div align="center">

### 🌟 Star this repository if you found it helpful!

<br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&duration=4000&pause=1000&color=38BDF8&center=true&vCenter=true&width=600&lines=Made+with+❤️+by+Mohammed+Usman;AI+for+Healthcare+🧠+💻;Open+Source+Medical+Diagnosis" alt="Footer" />

<br><br>

[![Stars](https://img.shields.io/github/stars/issu321/Brain-Tumor-Detection-ANN?style=social)](https://github.com/issu321/Brain-Tumor-Detection-ANN/stargazers)
[![Forks](https://img.shields.io/github/forks/issu321/Brain-Tumor-Detection-ANN?style=social)](https://github.com/issu321/Brain-Tumor-Detection-ANN/network/members)

</div>
