from flask import Blueprint, render_template, flash
from .forms import ManufacturerSearchForm,ManufacturerAddForm,ManufacturerEditForm
from sqlalchemy import func
from ..utils.helpers import is_admin
manufacturers = Blueprint('manufacturers',__name__)

from ..models import Manufacturer, LegalForm
from .. import db

@manufacturers.route("/manufacturers",methods=["GET", "POST"])
@is_admin
def manu_facturers():
    form_search = ManufacturerSearchForm()
    legal_forms = LegalForm.query.all()
    form_add = ManufacturerAddForm()
    form_add.manuf_legal_form.choices = [(i.id,i.name) for i in legal_forms]
    # Форма поиска
    if form_search.search_filter.data=="Все" and form_search.is_submitted():
        manuf_list = Manufacturer.query.all()
        return render_template("manufacturers/manufacturers.html",
                                form_search=form_search,
                                form_add=form_add,
                                manufacturers_list=manuf_list)
    elif form_search.find.data and form_search.validate():
        search_string = form_search.manuf_name_search.data.lower()
        if form_search.manuf_name_search.data not in (None,""):
            if form_search.search_filter.data=="Начинается с":
                search=f"{search_string}%"
            elif form_search.search_filter.data=="Содержит":
                search=f"%{search_string}%"
            else:
                search=f"%{search_string}"
        else:
            search=""
        manuf_list = Manufacturer.query.filter(func.lower(Manufacturer.name).like(search)).order_by(Manufacturer.name).all()
        return render_template("manufacturers/manufacturers.html",
                                form_search=form_search,
                                form_add=form_add,
                                manufacturers_list=manuf_list)
    # Форма добавления
    if form_add.add.data and form_add.validate():
        if Manufacturer.query.filter_by(name=form_add.manuf_name_add.data).first():
            form_add.manuf_name_add.errors.append("Производитель уже есть в базе")
            return render_template("manufacturers/manufacturers.html",
                        form_search=form_search,
                        form_add=form_add)
        manuf = Manufacturer(name=form_add.manuf_name_add.data,legal_form_id=form_add.manuf_legal_form.data)
        db.session.add(manuf)
        db.session.commit()
        flash("Производитель добавлен")
    return render_template("manufacturers/manufacturers.html",
                        form_search=form_search,
                        form_add=form_add)

@manufacturers.route("/manufacturers/<manufacturer_name>")
@is_admin
def edit_manufacturer(manufacturer_name):
    form_edit = ManufacturerEditForm()
    manufacturer = Manufacturer.query.filter_by(name=manufacturer_name).first()
    return render_template("manufacturers/manufacturer_page.html",manufacturer=manufacturer,form_edit=form_edit)
