from flask import session, render_template

def is_admin(f):
    def inner(*args,**kwargs):
        if session.get('role') != 'ADMIN':
            return render_template("forbidden.html"), 403
        else:
            return f(*args,**kwargs)
    inner.__name__=f.__name__
    return inner
