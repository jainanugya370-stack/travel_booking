# ✈️ Travel Booking Web Application

## 📌 Overview
This is a **Django-based Travel Booking Web Application** that allows users to browse travel options, register/login, and book trips.  
The project demonstrates full-stack development using Django with templates, authentication, and database integration.

---

## ✨ Features
- 🔐 User Registration & Login System  
- 🏠 Home page with available travel options  
- 📖 Book trips بسهولة  
- 📋 View "My Bookings"  
- 🧾 Form handling using Django Forms  
- 🗄️ SQLite database integration  
- 🎨 Clean UI using HTML templates  

---

## 🏗️ Tech Stack

### 💻 Backend
- Python
- Django

### 🎨 Frontend
- HTML
- CSS (basic styling)

### 🗄️ Database
- SQLite (default Django DB)

---

## 📂 Project Structure
```
travel_booking/
│
├── bookings/
│   ├── migrations/
│   ├── templates/
│   │   └── bookings/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── book.html
│   │       ├── login.html
│   │       ├── register.html
│   │       └── my_bookings.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── tests.py
│
├── travel_booking/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── db.sqlite3
```

---

## ⚙️ Installation & Setup

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/jainanugya370-stack/travel_booking.git
cd travel_booking
```

---

### 🔹 2. Create Virtual Environment
```bash
python -m venv .venv
```

Activate it:
```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

---

### 🔹 3. Install Dependencies
```bash
pip install django
```

---

### 🔹 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 🔹 5. Run Server
```bash
python manage.py runserver
```

---

## 🌐 Usage
1. Open browser → `http://127.0.0.1:8000/`  
2. Register a new user  
3. Login  
4. Book travel packages  
5. View your bookings  

---

##  Contributing
Contributions are welcome!

1. Fork the repository  
2. Create a branch  
```bash
git checkout -b feature-name
```
3. Commit changes  
```bash
git commit -m "Added feature"
```
4. Push  
```bash
git push origin feature-name
```
5. Open Pull Request  

---

## 📜 License
All Rights Reserved © 2026 Anugya Jain  

This project and its source code are the intellectual property of the author.  
Unauthorized use, copying, or distribution is prohibited.

---

## 💡 Author
**Anugya Jain**
