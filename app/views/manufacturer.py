from flask import Blueprint, render_template
from flask_login import login_required
from .forms import ManufacturerSearchForm,ManufacturerAddForm
from ..utils.helpers import is_admin
manufacturers = Blueprint('manufacturers',__name__)

@manufacturers.route("/manufacturers")
@login_required
@is_admin
def manu_facturers():
    form_search = ManufacturerSearchForm()
    form_add = ManufacturerAddForm()
    return render_template("manufacturers.html",form_search=form_search, form_add=form_add)

@manufacturers.route("/manufacturers/<manufacturer_name>")
@is_admin
def edit_manufacturer(manufacturer_name):
    pass
