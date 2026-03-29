# Community Issue Reporting System

A Django-based web application that allows community members to report local issues (such as water leaks, electricity problems, potholes, and waste management concerns) and track their resolution status.

## Features

### For Community Members
- **User Registration & Authentication** - Secure login and registration system
- **Issue Reporting** - Submit issues with detailed descriptions, photos, and location data
- **Issue Tracking** - Monitor the status of reported issues in real-time
- **Photo Uploads** - Attach images to provide visual evidence of issues
- **Location Support** - Include address and GPS coordinates for precise issue定位

### For Staff/Administrators
- **Staff Dashboard** - Centralized view of all reported issues
- **Status Management** - Update issue status (Pending, In Progress, Resolved)
- **Priority Assignment** - Set priority levels (Low, Medium, High)
- **Resolution Notes** - Add notes when resolving issues
- **Statistics Overview** - View counts of pending, in-progress, and resolved issues

## Tech Stack

- **Backend**: Django 6.0.2
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Django's built-in authentication system
- **Image Handling**: Django's ImageField with Pillow

## Project Structure

```
community_system/
├── community_system/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── reports/                   # Main app for issue reporting
│   ├── models.py              # Issue model
│   ├── views.py               # View functions
│   ├── urls.py                # URL routing
│   ├── forms.py               # Form definitions
│   └── templates/             # HTML templates
├── users/                     # User authentication app
│   ├── views.py               # Auth views
│   ├── urls.py                # Auth URLs
│   └── templates/             # Auth templates
├── media/                     # Uploaded files
├── staticfiles/               # Static assets
├── manage.py                  # Django management script
└── db.sqlite3                 # SQLite database
```

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/community-issue-reporting.git
   cd community-issue-reporting
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install django pillow
   ```

5. **Navigate to the project directory**
   ```bash
   cd community_system
   ```

6. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Reporting an Issue

1. Register an account or log in
2. Navigate to the "Report Issue" page
3. Fill in the issue details:
   - Issue type (Water, Electricity, Pothole, Waste, etc.)
   - Description
   - Photo (optional)
   - Address
   - GPS coordinates (optional)
4. Submit the report

### Tracking Issues

1. Log in to your account
2. Navigate to the "Track Issues" page
3. View all reported issues and their current status

### Staff Dashboard

1. Log in with a staff account
2. Navigate to the "Staff Dashboard"
3. View all issues with filtering options
4. Update issue status, priority, and add resolution notes

## Models

### Issue Model

| Field | Type | Description |
|-------|------|-------------|
| user | ForeignKey | User who reported the issue |
| issue_type | CharField | Type of issue |
| description | TextField | Detailed description |
| photo | ImageField | Optional photo attachment |
| address | CharField | Location address |
| latitude | CharField | GPS latitude |
| longitude | CharField | GPS longitude |
| status | CharField | Current status (Pending/In Progress/Resolved) |
| priority | CharField | Priority level (Low/Medium/High) |
| created_at | DateTimeField | Timestamp of creation |
| resolution_notes | TextField | Notes added when resolved |

## URL Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | report_issue | Home page / Report issue |
| `/report/` | report_issue | Report a new issue |
| `/track/` | track_issues | Track all issues |
| `/staff/` | staff_dashboard | Staff dashboard |
| `/login/` | LoginView | User login |
| `/register/` | register | User registration |
| `/logout/` | LogoutView | User logout |

## Configuration

### Media Files

Uploaded images are stored in the `media/issue_photos/` directory. Configure in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Static Files

Static assets are stored in `staticfiles/` directory:

```python
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django documentation and community
- Bootstrap for frontend styling inspiration
- Contributors and maintainers

## Contact

For questions or support, please open an issue on GitHub.

---

**Note**: This is a development project. For production deployment, ensure proper security configurations including:
- Changing the SECRET_KEY
- Setting DEBUG = False
- Configuring ALLOWED_HOSTS
- Using a production-grade database (PostgreSQL, MySQL)
- Setting up proper static file serving
- Implementing HTTPS
