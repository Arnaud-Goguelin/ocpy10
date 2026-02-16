# SoftDesk - Project manager

## 📖 About the Project

SoftDesk is a Django Restfull API for managing project. 
This project was developed as an exercise of a training program focused on mastering Django REST framework.

As it is just an exercise, a command is already provided to create two test users.
It will run automatically when the application is started in docker.

### Key Features

- **User Authentication**: Sign up, login, and logout functionality
- **Project Management**: Create and manage software development projects
- **Issue Tracking**: Create and track issues/bugs within projects
- **Contributor Management**: Add and manage contributors to your projects
- **Comments System**: Add comments to issues for better collaboration
- **Access Control**: Role-based permissions (author, contributor) for projects and issues

---

## 🚀 Quick Start

### Justfile
A [Justfile](https://github.com/casey/just) is provided to simplify the process of running.
Use the following command to show all available commands:
   ```bash
   just --list
   ```

Use the following command to run the application in a docker container:
   ```bash
   just docker-up
   # it runs: docker compose -f docker/compose.local.yml up --build
   ```

## 🐳 Quick Start with Docker (Recommended)

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed

### Running the Application

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ocpy10_softdesk
   ```

2. **Build and start the container**
   ```bash
   docker compose -f docker/compose.local.yml up --build
   ```

3. **Access the swagger**
   
   Open your browser and navigate to: [softdesk api swagger](http://127.0.0.1:8000/api/docs/swagger/)

4. **Test Users**
   
   Two test users are automatically created:
   - Username: `Bob` | Password: `softdesk_api`
   - Username: `Tom` | Password: `softdesk_api`

5. **Stop the application**
   ```bash
   docker compose -f docker/compose.local.yml down
   ```

### Data Persistence

The SQLite database is persisted in the `data/` directory.

---

## 💻 Local Development Setup

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ocpy10_softdesk
   ```

2. **Install dependencies with uv**
   ```bash
   uv sync
   ```

3. **Activate the virtual environment**
   
   - On Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```
   
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create test users (optional)**
   ```bash
   python manage.py create_test_users
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the swagger**
   
   Open your browser and navigate to: [softdesk api swagger](http://127.0.0.1:8000/api/docs/swagger/)

---

## 🛠️ Dependencies

- **Framework**: Django 5.2.8
- **API Framework**: Django REST Framework 3.16.1
- **Authentication**: djangorestframework-simplejwt 5.5.1
- **API Documentation**: drf-spectacular 0.29.0
- **Database**: SQLite3
- **Package Manager**: uv
- **ASGI Server**: Uvicorn 0.38.0
- **Testing**: pytest, pytest-django, pytest-cov
- **Code Quality**: Ruff 0.12.4 (formatter & linter)
- **Development Tools**: ipdb, Faker, factory-boy
---

## ⚠️ Important Notes

### Development Server

This application uses Django's built-in development server (`runserver`) for ease of evaluation and testing. **This setup is not suitable for production environments.**

### Security

The `SECRET_KEY` in `settings.py` is exposed for development purposes only. 
In a production environment, this should be stored securely as an environment variable.

---

## 🐛 Troubleshooting

### Docker Issues

**Permission denied errors**: Make sure Docker has proper permissions to access the project directory.

**Port 8000 already in use**: Stop any other services running on port 8000 or modify the port mapping in 
`docker/compose.local.yml`.

### Local Development Issues

**Module not found**: Ensure you've activated the virtual environment and run `uv sync`.

**Database errors**: Try deleting `data/db.sqlite3` and running `python manage.py migrate` again.

---

## 👤 Author
Arnaud Goguelin
