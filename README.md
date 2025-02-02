# 🌐 BharatAssignment: Multilingual FAQ Management System  

A Django-based backend system for managing FAQs with **automated translations**, **WYSIWYG editor support**, and a REST API. Built for the BharatFD hiring process.  

---

## 🚀 Key Features  
- **🌍 Multilingual Support**: FAQs auto-translated to Hindi (`hi`) and Bengali (`bn`) using Google Translate.  
- **📝 WYSIWYG Editor**: CKEditor integration for rich-text answers.  
- **⚡ REST API**: Fetch FAQs in any language via `?lang=` parameter.  
- **🔒 Admin Panel**: User-friendly interface for managing FAQs.  
- **🤖 Automation**: Translations generated automatically on FAQ creation.  

---

## 🛠️ Installation  

### 1️⃣ Clone the Repository  
git clone https://github.com/SrihithaJhansi/BharatFd_Assignment.git
-cd BharatFd_Assignment

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Configure Settings
Rename .env.example to .env.

Add your Google Translate API key (if using) or keep googletrans as default.

### 5️⃣ Run Migrations
python manage.py migrate

### 6️⃣ Create a Superuser (Admin Access)
python manage.py createsuperuser
Follow the prompts to set up an admin username and password.

### 7️⃣ Start the Server
python manage.py runserver
Visit http://127.0.0.1:8000 to explore!

📡 API Usage
Fetch FAQs

# English (default)
curl http://127.0.0.1:8000/api/faq/

# Hindi
curl http://127.0.0.1:8000/api/faq/?lang=hi

# Bengali
curl http://127.0.0.1:8000/api/faq/?lang=bn


🖥️ Admin Panel
Visit http://127.0.0.1:8000/admin.

🔑 Log in using your superuser credentials.

Add/Edit FAQs:
✅ Questions/answers are auto-translated to Hindi and Bengali on save.
✅ WYSIWYG editor allows rich-text formatting.

💡 Technologies Used
Backend: Django, Django REST Framework
Database: SQLite (default) / PostgreSQL
Translation: googletrans / Google Translate API
Editor: django-ckeditor


🤝 Contributing
Pull requests are welcome!

Follow PEP8 guidelines.
Write unit tests for new features.
Use conventional Git commit messages (e.g., feat: Add Hindi translation).
