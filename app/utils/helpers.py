from flask import session, render_template

def is_admin(f):
    def inner():
        print(session.get('role'))
        if session.get('role') != 'ADMIN':
            return render_template("forbidden.html"), 403
        else:
            return f()
    inner.__name__=f.__name__
    return inner
