##🚀 Fullstack User Control System (RBAC)



![Uploading image.png…]()


A production-ready full-stack web application built using React and Django, implementing Role-Based Access Control (RBAC) with secure authentication, protected routes, and an admin dashboard.





🌟 Key Highlights

✅ Secure JWT Authentication
✅ Role-Based Authorization (Admin / Manager / User)
✅ Scalable Backend Architecture
✅ Clean & Modular Frontend
✅ Admin Panel for User Management
✅ Production-Ready Structure

🧩 Features Overview
🔐 Authentication & Security

JWT Authentication (Access + Refresh Tokens)

Role-based route protection

Secure password handling

Token-based API access

👥 Role Management
Role	Permissions
Admin	Full system access, manage users & roles
Manager	Create and manage tasks
User	View assigned tasks only
⚙️ Tech Stack
🖥 Backend

Python

Django

Django REST Framework

SimpleJWT

SQLite / PostgreSQL

🎨 Frontend

React

React Router DOM

Axios

Context API

📂 Project Structure
project/
├── backend/
│   ├── core/
│   ├── users/
│   ├── manage.py
│   ├── requirements.txt
│   └── db.sqlite3
│
└── frontend/
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   ├── context/
    │   └── services/
    ├── public/
    └── package.json

🚀 Getting Started
🔧 Backend Setup
cd backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Backend will run on:

http://127.0.0.1:8000/

🎨 Frontend Setup
cd frontend
npm install
npm start


Frontend will run on:

http://localhost:3000/

🔐 Authentication Flow

User logs in using credentials

Backend issues JWT tokens

Tokens stored securely on frontend

Protected routes verify role & token

Access granted based on user role

🧪 Testing Guide

Login as Admin

Create users and assign roles

Logout and login as Manager/User

Verify access permissions

Try restricted routes to confirm protection

🖥 Admin Panel

Admin Dashboard allows:

User creation

Role assignment

Permission management

Access:

/admin

📸 Screenshots

Add screenshots here for better presentation

🚀 Future Enhancements

Email verification

Password reset via email

Docker & Docker Compose

Activity logs

CI/CD integration

API rate limiting

👨‍💻 Author

Shivam Yadav
🔗 GitHub: https://github.com/Shivam-123-yadav





