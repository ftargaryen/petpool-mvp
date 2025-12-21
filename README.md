# PetPool MVP 🐾
A premium social media platform for pet owners built with Django and Bootstrap 5.

## 🚀 Live Demo
The application is live and can be accessed here:
**[https://frank816.pythonanywhere.com/register/](https://frank816.pythonanywhere.com/register/)**

## ✨ Key Features
- **User Authentication**: Secure registration and login system.
- **Pet Management**: Relational profiles for pets linked to their owners.
- **Social Feed**: A dynamic feed where users can share photos and captions of their pets.
- **Search Functionality**: A search engine to filter posts by caption or owner.
- **Modern UI**: A responsive, purple-themed interface using Font Awesome icons.

## 📊 Database Architecture (Deliverable #2)
The project utilizes a relational SQLite database with the following schema design:

| Table | Relationship | Key Fields |
| :--- | :--- | :--- |
| **User** | Parent | `username`, `password`, `email` |
| **Pet** | Many-to-One (User) | `name`, `species`, `bio`, `owner_id` (FK) |
| **Post** | Many-to-One (User) | `caption`, `image`, `created_at`, `author_id` (FK) |



## 🛠️ Tech Stack
- **Backend**: Django 5.1 / Python 3.10
- **Frontend**: Bootstrap 5, Font Awesome
- **Deployment**: PythonAnywhere
