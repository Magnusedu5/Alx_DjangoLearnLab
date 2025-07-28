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