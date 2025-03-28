# Customizing the Django Admin with SimpleUI for a Sleek, Modern Interface

This project provides a comprehensive guide to upgrading your Django admin panel using **SimpleUI**, a modern and customizable admin interface. Additionally, we will implement user authentication (JWT-based login & signup), secure password hashing with **Argon2**, soft-delete functionality, **Redis caching**, and a PostgreSQL database. The project also includes a CRUD implementation for an e-commerce store using **Drizzle ORM**.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation and Setup](#installation-and-setup)
   - 4.1 [Setting Up Django Project](#setting-up-django-project)
   - 4.2 [Installing SimpleUI](#installing-simpleui)
   - 4.3 [Configuring PostgreSQL](#configuring-postgresql)
   - 4.4 [Adding Redis Caching](#adding-redis-caching)
   - 4.5 [User Authentication (JWT, Argon2, Soft-Delete)](#user-authentication-jwt-argon2-soft-delete)
   - 4.6 [CRUD Functionality for E-commerce Store](#crud-functionality-for-e-commerce-store)
5. [Running the Application](#running-the-application)
6. [Contributing](#contributing)
7. [License](#license)

---

## Introduction

The Django admin panel is a powerful tool for managing your application's backend. However, its default interface can feel outdated and lack customization options. **SimpleUI** enhances the admin panel with a sleek, modern design and additional features like dark mode, custom themes, and responsive layouts.

This project demonstrates how to integrate SimpleUI into a Django project while implementing advanced features such as JWT-based authentication, secure password hashing, soft-delete functionality, Redis caching, and CRUD operations for an e-commerce store.

---

## Features

- **Modern Admin Interface**: Upgrade the Django admin panel with SimpleUI for a sleek and responsive design.
- **User Authentication**:
  - JWT-based login and signup for secure API authentication.
  - Password hashing using **Argon2** for enhanced security.
  - Soft-delete functionality to prevent permanent data loss.
- **Database Management**:
  - PostgreSQL as the primary database.
  - Drizzle ORM for efficient database interactions.
- **Performance Optimization**:
  - Redis caching to improve response times and reduce server load.
- **E-commerce CRUD**:
  - Implement CRUD operations for an e-commerce store (Products, Categories, Orders, etc.).

---

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- PostgreSQL
- Redis
- Node.js and npm (for Drizzle ORM)
- Virtual environment tool (e.g., `venv` or `virtualenv`)

---

## Installation and Setup

### Setting Up Django Project

1. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Django**:
   ```bash
   pip install django
   ```

3. **Create a New Django Project**:
   ```bash
   django-admin startproject ecommerce_project
   cd ecommerce_project
   ```

4. **Start a New App**:
   ```bash
   python manage.py startapp store
   ```

### Installing SimpleUI

1. **Install SimpleUI**:
   ```bash
   pip install django-simpleui
   ```

2. **Add SimpleUI to Installed Apps**:
   In `settings.py`, add `'simpleui'` to the `INSTALLED_APPS` list:
   ```python
   INSTALLED_APPS = [
       'simpleui',
       ...
   ]
   ```

3. **Customize SimpleUI**:
   You can customize the admin theme by modifying the `SIMPLEUI_CONFIG` dictionary in `settings.py`:
   ```python
   SIMPLEUI_CONFIG = {
       'system_keep': True,
       'menu_display': ['store'],
       'theme': 'dark',  # Options: 'light', 'dark'
   }
   ```

### Configuring PostgreSQL

1. **Install PostgreSQL Driver**:
   ```bash
   pip install psycopg2-binary
   ```

2. **Update Database Settings**:
   In `settings.py`, configure the database connection:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'ecommerce_db',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### Adding Redis Caching

1. **Install Redis Client**:
   ```bash
   pip install redis django-redis
   ```

2. **Configure Redis in Django**:
   Update `settings.py` with Redis cache settings:
   ```python
   CACHES = {
       'default': {
           'BACKEND': 'django_redis.cache.RedisCache',
           'LOCATION': 'redis://127.0.0.1:6379/1',
           'OPTIONS': {
               'CLIENT_CLASS': 'django_redis.client.DefaultClient',
           }
       }
   }
   ```

3. **Use Redis for Session Storage**:
   Add the following to `settings.py`:
   ```python
   SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
   SESSION_CACHE_ALIAS = 'default'
   ```

### User Authentication (JWT, Argon2, Soft-Delete)

1. **Install Required Packages**:
   ```bash
   pip install djangorestframework djangorestframework-simplejwt argon2-cffi django-model-utils
   ```

2. **Configure JWT Authentication**:
   Add the following to `settings.py`:
   ```python
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ),
   }
   ```

3. **Set Up Argon2 Password Hasher**:
   Update `settings.py`:
   ```python
   PASSWORD_HASHERS = [
       'django.contrib.auth.hashers.Argon2PasswordHasher',
       ...
   ]
   ```

4. **Implement Soft-Delete**:
   Use `django-model-utils` to add soft-delete functionality:
   ```python
   from model_utils.models import SoftDeletableModel

   class Product(SoftDeletableModel):
       name = models.CharField(max_length=255)
       price = models.DecimalField(max_digits=10, decimal_places=2)
   ```

### CRUD Functionality for E-commerce Store

1. **Define Models**:
   Create models for `Product`, `Category`, and `Order` in `store/models.py`.

2. **Migrate Models**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Set Up Drizzle ORM**:
   Install Drizzle CLI:
   ```bash
   npm install drizzle-kit --save-dev
   ```

   Configure Drizzle in your project and generate SQL migrations.

4. **Implement CRUD Views**:
   Use Django REST Framework to create API views for CRUD operations.

---

## Running the Application

1. **Start Redis Server**:
   ```bash
   redis-server
   ```

2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Start Django Development Server**:
   ```bash
   python manage.py runserver
   ```

4. **Access the Admin Panel**:
   Navigate to `http://127.0.0.1:8000/admin` and log in with your superuser credentials.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
