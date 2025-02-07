# 🚀 AI-Powered Hashtag Generator - Django Backend  

🔍 **Django REST API for AI-driven hashtag suggestions**  

## 🔗 Live API URL (Vercel)
🌍 **Backend:** [https://your-vercel-project.vercel.app](https://your-vercel-project.vercel.app)  

---

## 📌 Features
✅ **AI-Powered Hashtag Suggestions** (Using OpenAI API)  
✅ **SEO-Optimized Hashtags** for Instagram & Facebook  
✅ **JWT Authentication** (User Login, Signup, Email Verification)  
✅ **Django REST Framework (DRF) API**  
✅ **MySQL Database (Clever Cloud)**  
✅ **Vercel Deployment**  

---

## ⚙️ Tech Stack
- **Framework**: Django, Django REST Framework (DRF)  
- **Authentication**: JWT (JSON Web Token)  
- **AI Processing**: OpenAI API  
- **Database**: MySQL (Clever Cloud)  
- **Deployment**: Vercel  

---

## 🚀 Getting Started  

### 🔹 1. Clone Repository
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 🔹 2. Setup Virtual Environment
```sh
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate
```

### 🔹 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 🔹 4. Configure Environment Variables
Create a **`.env`** file in the **root directory** and add:
```env
# OpenAI API Key
OPENAI_KEY=sk-xxxxxxxxxxxxxxxxxxxx

# MySQL Database Credentials (Clever Cloud)
CC_MYSQL_DATABASE=your-database
CC_MYSQL_USER=your-username
CC_MYSQL_PASSWORD=your-password
CC_MYSQL_HOST=your-host
CC_MYSQL_PORT=3306

# Email Configuration
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Django Secret Key
SECRET_KEY=your-django-secret-key
```

### 🔹 5. Run Migrations & Start Server
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 📬 API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| **POST** | `/api/auth/register/` | Register a new user |
| **POST** | `/api/auth/login/` | User login & JWT authentication |
| **POST** | `/api/hashtags/generate/` | Generate AI-powered hashtags |
| **POST** | `/api/hashtags/save/` | Save hashtags for later |

---

## 🚀 Deployment on Vercel  

1️⃣ **Push Code to GitHub**
```sh
git add .
git commit -m "Initial Django backend commit"
git push origin main
```

2️⃣ **Deploy to Vercel**
- Go to [**Vercel Dashboard**](https://vercel.com/)  
- Import **GitHub Repository**  
- Configure Environment Variables  
- Set **Build Command**:  
  ```sh
  pip install -r requirements.txt && python manage.py collectstatic --noinput
  ```
- Set **Start Command**:  
  ```sh
  gunicorn backend.wsgi
  ```
- **Deploy & Test** 🚀  

---

🔥 **Like the project? Give it a ⭐ on GitHub!**  
📩 Need Help? Contact Rayapputhanusiyan25062000@gmail.com
