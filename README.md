# 📁 Django File Ownership Transfer API

This Django REST API allows authenticated users to upload files, transfer file ownership to other users, and revoke those transfers. Every action is tracked with a full transfer history log.

---

## 🚀 Features

- 🔐 User authentication (Basic Auth)
- 📤 File upload with automatic ownership assigned
- 🔁 Transfer file ownership to another user
- 🔙 Revoke file transfer to reclaim ownership
- 🕓 Full transfer and revoke history with timestamps
- 🧾 Django admin panel for managing users, files, and history

---

## 🏗️ Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite3 (default database)

---

## 📦 Setup Instructions

### 1. Clone or Download the Project and go to the base directory

### 2. Create and Activate a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
````

---

### 2. Install Django and Django REST Framework

```bash
pip install django djangorestframework
```

---

### 3. Run Migrations and Create a Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

### 4. Start the Server

```bash
python manage.py runserver
```

---

## 🔑 API Endpoints

| Method | Endpoint         | Description                   | Auth Required |
| ------ | ---------------- | ----------------------------- | ------------- |
| POST   | `/api/upload/`   | Upload a file                 | ✅ Yes         |
| POST   | `/api/transfer/` | Transfer file to another user | ✅ Yes         |
| POST   | `/api/revoke/`   | Revoke a file transfer        | ✅ Yes         |

---

## 📋 Request Format

### 🔸 Transfer File Example

```json
{
  "file_id": 1,
  "to_user_id": 2
}
```

### 🔸 Revoke File Example

```json
{
  "file_id": 1
}
```

> 🛡️ All requests require Basic Auth using a valid username and password.

---

## 🧪 Testing with Postman

Used [Postman](https://www.postman.com/) to test all API endpoints.

