# Conecta ZL - Portal de Notícias

## Overview
Conecta ZL is a community news portal developed in Django, focused on connecting the East Zone (Zona Leste) of São Paulo with local relevant information. The platform allows local journalists to publish content and enables community interaction through comments and likes.

**Status**: Running successfully on Replit with Django 5.2.8
**Last Updated**: December 2, 2025

## Project Architecture

### Framework & Stack
- **Backend**: Django 5.2.8 (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript with TailwindCSS
- **Database**: SQLite (development), PostgreSQL (production)
- **Static Files**: WhiteNoise for static file serving
- **Rich Text Editor**: django-summernote
- **Maps**: Folium for interactive geolocation
- **API**: Django REST Framework

### Key Applications
1. **users**: User authentication, profiles with roles (reader, journalist, admin)
2. **articles**: News articles with approval workflow, likes, views, tags
3. **comments**: Comment system with moderation
4. **api**: RESTful API for external integrations

### Database Schema
- User profiles with role-based permissions (leitor, jornalista, admin)
- Articles with approval status (pending, approved, rejected)
- Comments with moderation flags
- Tags for article categorization
- Like system for articles
- Geolocation data for news articles

## Recent Changes (December 2, 2025)
- Added missing dependencies: dj-database-url, whitenoise
- Configured for Replit environment with port 5000
- Ran initial migrations successfully
- Set up static files collection
- Created media directories for user uploads
- Configured workflow for Django development server

## Configuration

### Environment Variables
- `DEBUG`: Set to True for development
- `SECRET_KEY`: Django secret key
- `ALLOWED_HOSTS`: Set to * for development
- `DATABASE_URL`: PostgreSQL URL (optional, falls back to SQLite)

### Port Configuration
- Development server runs on **0.0.0.0:5000** (required for Replit)
- Frontend accessible via webview

### Static & Media Files
- Static files: `/static/` and `/staticfiles/` (collected)
- Media uploads: `/media/` (articles, profiles, banners)
- WhiteNoise handles static file serving in production

## User Roles & Permissions

### Leitor (Reader)
- View published articles
- Comment on articles
- Like articles
- View journalist profiles

### Jornalista (Journalist)
- All reader permissions
- Create articles (status: pending)
- Edit own articles
- Upload images
- Add tags and geolocation
- Manage profile with banner and avatar

### Admin (Administrator)
- All journalist permissions
- Approve/reject articles
- Moderate comments
- Manage users
- Access Django admin panel
- View dashboard with statistics

## Development Commands

```bash
# Run server
python manage.py runserver 0.0.0.0:5000

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Run tests
python manage.py test
```

## API Endpoints
- `/api/articles/` - List and create articles
- `/api/articles/{slug}/` - Article detail, update, delete
- `/api/comments/` - Comments management

## Features
- Article approval workflow for quality control
- Rich text editor with image uploads
- Interactive maps for geolocated news
- Tag-based article organization
- Like and view counting
- User profiles with customizable banners
- Responsive design for mobile and desktop
- RESTful API for integrations

## Project Structure
```
portal_noticias/    # Django settings and URLs
users/              # User management and profiles
articles/           # Article CRUD and admin dashboard
comments/           # Comment system
api/                # REST API
templates/          # HTML templates
static/             # CSS, JS, images
media/              # User uploads
```

## User Preferences
None recorded yet.
