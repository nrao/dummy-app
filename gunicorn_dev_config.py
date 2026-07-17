
from glob import glob


reload = True
reload_extra_files = glob("src/dummy_app/templates/*") + glob("src/dummy_app/static/*") + [
    ".env"
]

accesslog = "-"
access_log_format = "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sμs"
