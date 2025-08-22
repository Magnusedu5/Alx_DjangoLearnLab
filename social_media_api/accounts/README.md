Social Media API

A RESTful API built with Django and Django REST Framework (DRF) that provides the foundation for a social media platform.
It includes user registration, authentication, profile management, and will later support posts, likes, and comments.

🚀 Features

User registration with custom user model (bio, profile picture, followers).

Token-based authentication using Django REST Framework.

User login with token retrieval.

Profile management (view and update authenticated user’s profile).

Ready for future extensions (posts, comments, likes, etc.).

🛠️ Tech Stack

Backend: Django, Django REST Framework

Authentication: DRF Token Authentication

Database: SQLite (default, can be changed to PostgreSQL/MySQL)

Python version: 3.9+ (recommended)

📂 Project Structure
social_media_api/
│── accounts/          # Handles user-related functionality
│   ├── models.py      # Custom User model
│   ├── serializers.py # User & registration serializers
│   ├── views.py       # Register, login, profile views
│   ├── urls.py        # Accounts-related routes
│
│── social_media_api/  # Project configuration
│   ├── settings.py    # Project settings
│   ├── urls.py        # Main URL routes
│
│── manage.py

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/yourusername/social_media_api.git
cd social_media_api

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py makemigrations
python manage.py migrate

5. Create a superuser (admin)
python manage.py createsuperuser

6. Run the development server
python manage.py runserver

🔑 API Endpoints
Endpoint	Method	Description	Auth Required
/api/accounts/register/	POST	Register a new user	❌
/api/accounts/login/	POST	Login & retrieve token	❌
/api/accounts/profile/	GET	Get logged-in user profile	✅
/api/accounts/profile/	PUT/PATCH	Update logged-in user profile	✅
📌 Example Requests
Register
POST /api/accounts/register/
Content-Type: application/json

{
  "username": "magnus",
  "email": "magnus@example.com",
  "password": "mypassword123"
}

Login
POST /api/accounts/login/
Content-Type: application/json

{
  "username": "magnus",
  "password": "mypassword123"
}


Response:

{
  "token": "abc123xyz...",
  "user": {
    "id": 1,
    "username": "magnus",
    "email": "magnus@example.com",
    "bio": "",
    "profile_picture": null
  }
}

Get Profile
GET /api/accounts/profile/
Authorization: Token abc123xyz...

📖 Next Steps (Future Features)

Posts (create, update, delete, view timeline)

Likes & Comments

Followers/Following relationships

Notifications

Direct messaging

👨🏽‍💻 Author

Magnus Edu
🚀 Aspiring Software Developer | 🌍 Passionate about solving real-world problems with technology