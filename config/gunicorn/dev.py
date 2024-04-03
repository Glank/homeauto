# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "homeauto.wsgi:application"
# The granularity of Error log outputs
loglevel = "warn"
# The number of worker processes for handling requests
workers = 2
# The socket to bind
bind = "0.0.0.0:8000"
# Restart workers when code changes? (No, because I test on a different port.)
reload = False
# Write access and error info to /var/log
accesslog = errorlog = "/var/log/gunicorn/dev.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "/run/gunicorn/dev.pid"
# Daemonize the Gunicorn process (detach & enter background)
# not used because running as a service, which is automatically daemonized
#daemon = True
