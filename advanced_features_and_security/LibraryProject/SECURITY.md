Security Implementation Overview
CSRF Protection: Implemented via {% csrf_token %} in all POST forms and enforced by Django's CsrfViewMiddleware.

SQL Injection Prevention: All database interactions use Django's ORM (Object-Relational Mapper) which uses query parameterization.

XSS Protection: Enhanced by setting SECURE_BROWSER_XSS_FILTER = True and using Django's template engine, which auto-escapes HTML characters.

Clickjacking: Prevented by X_FRAME_OPTIONS = 'DENY'.

Input Validation: All user-provided data is validated through Django Forms to ensure it matches expected types/formats.