from flask import Blueprint,render_template
from ..utils.helpers import is_admin

admin = Blueprint('admin',__name__)

@admin.route('/adminpage')
@is_admin
def adminpage():
    return render_template('adminpage.html')