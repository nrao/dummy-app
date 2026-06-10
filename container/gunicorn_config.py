
import os


workers = int(os.environ.get("GUNICORN_PROCESSES", 1))
threads = int(os.environ.get("GUNICORN_THREADS", 4))
bind = os.environ.get("GUNICORN_BIND", "0.0.0.0:5000")

accesslog = "-"
access_log_format = "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sμs"
