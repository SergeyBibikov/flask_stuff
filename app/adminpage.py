from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from .models import User, Product, Manufacturer,Order,Country,LegalForm,Category

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return is_admin()
        
class UserView(ModelView):
    column_searchable_list = ['username','email','id']
    can_create=False
    can_edit=False
    can_delete=False
    column_display_pk = True

    def is_accessible(self):
        return is_admin()

class ProductView(ModelView):
    column_searchable_list = ['name','manufacturer_id','id']
    form_excluded_columns =['cart_stats_rel','order_item_rel']
    column_display_pk = True

    def is_accessible(self):
        return is_admin()

class ManufacturerView(ModelView):
    column_searchable_list = ['name','id']
    form_excluded_columns = ['products_rel']
    column_display_pk = True

    def is_accessible(self):
        return is_admin()

class OrderView(ModelView):
    column_searchable_list = ['id']
    can_create=False
    can_edit=False
    can_delete=False
    column_display_pk = True

    def is_accessible(self):
        return is_admin()

class CountryView(ModelView):
    column_searchable_list = ['name','id']
    form_excluded_columns = ['products_rel']
    column_display_pk = True

    def is_accessible(self):
        return is_admin()

class LegalFormView(ModelView):
    column_searchable_list = ['name','id']
    column_display_pk = True
    form_excluded_columns = ['legal_forms_rel']
    def is_accessible(self):
        return is_admin()

class CategoryView(ModelView):
    column_searchable_list = ['name','id']
    form_excluded_columns = ['products_rel']
    column_display_pk = True
    def is_accessible(self):
        return is_admin()

def is_admin():
    try:
        role_id = current_user.role_id
    except AttributeError:
        return False
    return role_id==2
    

def return_all_views(session):
    return [ProductView(Product,session),
            UserView(User,session),
            ManufacturerView(Manufacturer,session),
            OrderView(Order,session),
            CountryView(Country,session),
            LegalFormView(LegalForm,session),
            CategoryView(Category,session)]