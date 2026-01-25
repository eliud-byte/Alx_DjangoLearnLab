Security Implementation Report
1. Data Transit Protection (HTTPS)

Mechanism: Enabled SECURE_SSL_REDIRECT.

Effect: Forces all traffic to be encrypted. If a user types http://, they are automatically moved to https://.

HSTS: Set strict transport security for 1 year. This prevents "Downgrade Attacks" where a hacker tries to force a user onto an unsecured connection.

2. Cookie Integrity

Mechanism: Set SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE to True.

Effect: Cookies containing sensitive session IDs or CSRF tokens will never be transmitted if the connection is not encrypted, preventing session hijacking over public Wi-Fi.

3. Browser-Side Defenses

XSS Filter: SECURE_BROWSER_XSS_FILTER is enabled to trigger legacy browser protections.

Content Sniffing: SECURE_CONTENT_TYPE_NOSNIFF prevents the browser from executing a text file as a script (a common upload vulnerability).

Clickjacking: X_FRAME_OPTIONS = 'DENY' ensures the library site cannot be loaded inside an invisible iframe on a malicious site, tricking users into clicking buttons they didn't intend to.