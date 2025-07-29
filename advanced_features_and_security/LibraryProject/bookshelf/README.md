# Django Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model:
- `can_view`: View book records
- `can_create`: Add new book
- `can_edit`: Modify book details
- `can_delete`: Remove a book

## Groups
- **Viewers**: Has `can_view`
- **Editors**: Has `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

## Usage
- Assign users to groups in Django Admin.
- Views are protected using `@permission_required`.
- Users will receive 403 error if they attempt unauthorized access.

## Security Measures Implemented

- CSRF Protection via {% csrf_token %}
- SQL Injection Prevention using Django ORM
- Secure headers (XSS filter, content-type sniffing, etc.)
- HTTPS-only cookies for sessions and CSRF
- Content Security Policy via django-csp

# Security Configuration: advanced_features_and_security

## HTTPS Enforcement
- `SECURE_SSL_REDIRECT = True`: All HTTP requests are redirected to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Forces browsers to use HTTPS for 1 year.
- HSTS applied to subdomains and preload enabled.

## Secure Cookies
- `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE`: Cookies sent only via HTTPS.

## Security Headers
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
- `SECURE_BROWSER_XSS_FILTER`: Enables XSS protection.
- `SECURE_CONTENT_TYPE_NOSNIFF`: Prevents MIME sniffing attacks.

## Deployment Notes
- Use Nginx with SSL (e.g., Let's Encrypt).
- All certificates stored at `/etc/letsencrypt/`.
- Redirect HTTP to HTTPS and proxy requests to Gunicorn or uWSGI.
