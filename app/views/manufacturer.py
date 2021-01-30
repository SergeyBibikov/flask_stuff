from flask import Blueprint, render_template, flash
from .forms import ManufacturerSearchForm,ManufacturerAddForm
from ..utils.helpers import is_admin
manufacturers = Blueprint('manufacturers',__name__)

from ..models import Manufacturer
from .. import db

@manufacturers.route("/manufacturers",methods=["GET", "POST"])
@is_admin
def manu_facturers():
    form_search = ManufacturerSearchForm()
    form_add = ManufacturerAddForm()
    if form_search.validate_on_submit():
        manuf_list = Manufacturer.query.filter_by(name=form_search.manuf_name_search.data)
        return render_template("manufacturers/manufacturers.html",
                                form_search=form_search,
                                form_add=form_add,
                                manufacturers_list=manuf_list)
    if form_add.validate_on_submit():
        manuf = Manufacturer(name=form_add.manuf_name_add.data)
        db.session.add(manuf)
        db.session.commit()
        flash("Производитель добавлен")
    return render_template("manufacturers/manufacturers.html",form_search=form_search, form_add=form_add)

@manufacturers.route("/manufacturers/<manufacturer_name>")
@is_admin
def edit_manufacturer(manufacturer_name):
    pass
