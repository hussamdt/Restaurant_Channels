from django.contrib import admin
from .models import *
from .forms import *


class Menu_ItemAdmin(admin.ModelAdmin):
    form= Menu_ItemForm
admin.site.register(Menu_Item,Menu_ItemAdmin)

admin.site.register(materials)

class MenuAdmin(admin.ModelAdmin):
    form= MenuForm
admin.site.register(Menu,MenuAdmin)


class TableAdmin(admin.ModelAdmin):
    form= TableForm
admin.site.register(Table,TableAdmin)


class oredr_itemAdmin(admin.ModelAdmin):
    form= Order_ItemForm
admin.site.register(Order_Item,oredr_itemAdmin)


class OrderAdmin(admin.ModelAdmin):
    form= OrderForm
   # الدالة التالية مسؤولة عن اعطاء خلفية زرقاء لبنود المنيو لطلبهن الزبون و الموجودين في صندوق اسمه أوردر آيتم تابع لكلاس الأورد في صفحة الأدمن بانل 
    def formfield_for_manytomany(self, db_field, request, **kwargs):# وأيضا يجب العلاقة أن تكون ماني تو ماني في سطر أورد آيتم من كلاس الأوردر من صفحة المودلز
        if db_field.name == "order_food_item":
            parent_id = request.resolver_match.kwargs.get("object_id")#وظيفة هذا السطر عندما أنت في الأدمن بانل تضغط على أحد الأشياء المحفوظة داخل كلاس أورد فان رقم الأورد يظهر فوق في مستطيل البراوسر
            try :
                x = Order.objects.get(pk=parent_id).order_food_item.all()
                kwargs["queryset"] =  x #الكويري سيت هو كل شيء داخل مستطيل الأوردر آيتم تبع كلاس أوردر من صفحة الأدمن بانل
            except :
                kwargs["queryset"] = Order_Item.objects.all()
        return super(OrderAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
admin.site.register(Order ,OrderAdmin )


