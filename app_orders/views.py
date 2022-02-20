from django.http.response import HttpResponse 
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView , DetailView  , DeleteView , UpdateView ,CreateView
from django.views import View
from django.urls import reverse
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Custom come to the table
# order pizza by the app
# waiter recieved the order and confirm it,
    # waiter can see all unconfirmed orders

# order will be in kitchen and cashier
    # cashier can see the status of order

# when the chef finish cooking will infrom the waiter to pickup


## Api Endpoint ( Rest Api )


class OurMenu(DetailView):
    model = Table # معناها أننا سوف نشتغل على كلاس ال التيبل من صفحة المودلز.باي لنحدد رقم الطاولة التي طلبت الأوردر 
    template_name =  "our_menu.html"
    context_object_name = "our_menu" # هو الاسم الذي يتم ارساله الى التمبلت فمثلا سوف ترى بعض التمبلتز تحتوي على فور اكس إن ثم الكلام الموجود في هذا السطر على يمين اليساوي  


class AddOrder(View): 
    def post(self, request, *args, **kwargs):
        table = request.POST["table"] # البوست معناه انه يكون ظاهر في مستطيل البراوسر 
        food_number = request.POST["food_number"]    # number=id or pk
        count = request.POST["count"]
        order_if_exsist = request.POST.get('order_id', False) # الفولس معناه انه رقم الأوردر لا يكون ظاهر في مستطيل البراوسر
        
        y = Order_Item()
        y.count = count 
        y.food_item = Menu_Item.objects.get(pk=food_number)
        y.save()

        if order_if_exsist :
            x = Order.objects.get(pk=order_if_exsist)
            x.order_food_item.add(y.pk)
        else :
            x= Order()
            x.table = Table.objects.get(number=table)
            x.save()  
            x.order_food_item.add(y.pk)


        messages.add_message(request, messages.INFO, f'You have added {count} {y.food_item.name} to your cart')

        return redirect('app_orders:our_menu_after', pk= table,  status='new-order' , order_id=x.id)


class Checkout(DetailView):
    model = Order
    context_object_name = 'checkout'
    template_name = "checkout.html" 
  


class DeleteOrderItem(DeleteView):
    model = Order_Item
    template_name = "delete_order_item.html"
    def get_success_url(self):
        theid = self.kwargs['pk']  
        theorder = Order.objects.get(order_food_item=theid)
        return reverse_lazy('app_orders:checkout', kwargs={'pk': theorder.pk})


class ConfirmOrderByUser(View): #  هل هذا CBV or FBV ??
    def get(self, request, *args, **kwargs):
        x = Order.objects.get(pk=kwargs['pk'])
        x.has_confirmed_by_user = True
        x.save()
        return HttpResponse('done')
        

class YesWaiterConfirmedOrderDeliveredOrder(ListView):
    model = Order
    template_name = "YesWaiterConfirmedOrderDeliveredOrder.html"
    context_object_name = "orders"

    def get_queryset(self):
        return self.model.objects.filter(has_confirmed_by_user=True , has_confirmed_by_waiter=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['deleviry'] = self.model.objects.filter(order_food_item__has_confirmed_by_cheif = True , order_food_item__has_been_delivered= False )
        context['deleviry'] = Order_Item.objects.filter(has_confirmed_by_cheif = True , has_been_delivered= False )
        return context

    def dispatch(self, *args, **kwargs):
        if self.request.user.groups.filter(name='waiter'):
            pass
        else:
            return HttpResponse('you are not allowed here')
            
        return super(YesWaiterConfirmedOrderDeliveredOrder, self).dispatch(*args, **kwargs)
        

class YesChefCookedOrder_kitchen1(ListView): 
    model = Order
    template_name = "YesChefCookedOrder.html"
    context_object_name = "orders"
    def get_queryset(self): 
        return Order_Item.objects.filter( food_item__kitchen_type = 'kitchen 1' , has_confirmed_by_cheif=False)
    

    def dispatch(self, *args, **kwargs):
        self.request.session['kitchen'] = 'YesChefCookedOrder_kitchen1'
        if self.request.user.groups.filter(name='chef'):
            pass
        else:
            return HttpResponse('you are not allowed here')
            
        return super(YesChefCookedOrder_kitchen1, self).dispatch(*args, **kwargs)

class YesChefCookedOrder_kitchen2(ListView): 
    model = Order
    template_name = "YesChefCookedOrder.html"
    context_object_name = "orders"
    def get_queryset(self): 
        return Order_Item.objects.filter( food_item__kitchen_type = 'kitchen 2' , has_confirmed_by_cheif=False)

    def dispatch(self, *args, **kwargs):
        self.request.session['kitchen'] = 'YesChefCookedOrder_kitchen2'
        if self.request.user.groups.filter(name='chef'):
            pass
        else:
            return HttpResponse('you are not allowed here')
            
        return super(YesChefCookedOrder_kitchen2, self).dispatch(*args, **kwargs)

class YesChefCookedOrder_kitchen3(ListView): 
    model = Order
    template_name = "YesChefCookedOrder.html"
    context_object_name = "orders"
    def get_queryset(self): 
        return Order_Item.objects.filter( food_item__kitchen_type = 'kitchen 3' , has_confirmed_by_cheif=False)

    def dispatch(self, *args, **kwargs):
        self.request.session['kitchen'] = 'YesChefCookedOrder_kitchen3'
        if self.request.user.groups.filter(name='chef'):
            pass
        else:
            return HttpResponse('you are not allowed here')
            
        return super(YesChefCookedOrder_kitchen3, self).dispatch(*args, **kwargs)




class HasWaiterConfirmedOrder(UpdateView):
    model = Order
    template_name = "HasWaiterConfirmedOrder.html"
    fields = ['has_confirmed_by_waiter']
    success_url  = reverse_lazy('app_orders:YesWaiterConfirmedOrderDeliveredOrder')

    def dispatch(self, *args, **kwargs):
        if self.request.user.groups.filter(name='waiter'):
            pass
        else:
            return HttpResponse('you are not allowed here')
          
        return super(HasWaiterConfirmedOrder, self).dispatch(*args, **kwargs)

    

class HasWaiterDeliveredOrder(UpdateView):
    model = Order_Item
    template_name = "HasWaiterDeliveredOrder.html"
    fields = ['has_been_delivered']
    success_url  = reverse_lazy('app_orders:YesWaiterConfirmedOrderDeliveredOrder')

    def dispatch(self, *args, **kwargs):
        if self.request.user.groups.filter(name='waiter'):
            pass
        else:
            return HttpResponse('you are not allowed here')
            
        return super(HasWaiterDeliveredOrder, self).dispatch(*args, **kwargs)


class HasChefCookedOrder(UpdateView):
    model = Order_Item
    template_name = "HasChefCookedOrder.html"
    fields = ['has_confirmed_by_cheif']
    # success_url  = reverse_lazy('app_orders:YesChefCookedOrder_kitchen1')
    def get_success_url(self):
        return reverse_lazy(f'app_orders:{self.request.session["kitchen"]}')

    def dispatch(self, *args, **kwargs):
        if self.request.user.groups.filter(name='chef'):
            pass
        else:
            return HttpResponse('you are not allowed here')

        return super(HasChefCookedOrder, self).dispatch(*args, **kwargs)


class OrderDetails(DetailView):
    model = Order
    template_name = "OrderDetails.html"
    context_object_name = "order"



class YesCashierOrder(ListView):
    model = Order 
    template_name = "YesCashierOrder.html"
    context_object_name = "orders"
    
    def get_queryset(self): 
        return self.model.objects.filter(has_confirmed_by_waiter=True , has_been_paid=False)


class HasCashierPrintOrder(DetailView):
    model = Order
    template_name = "HasCashierPrintOrder.html"
    context_object_name = "the_order"



class ConfirmPaidByCashier(View): 
    def get(self, request, *args, **kwargs):
        x = Order.objects.get(pk=kwargs['pk'])
        x.has_been_paid = True
        x.save()
        return HttpResponse('done')



################################################

class Menu_ItemListView(ListView):
    model = Menu_Item
    template_name = "Menu_ItemListView.html"
    context_object_name = 'menu_items'

class Menu_ItemDeleteView(DeleteView):
    model = Menu_Item
    template_name = "delete.html"
    success_url  = reverse_lazy('app_orders:Menu_ItemListView')

class Menu_ItemUpdateView(UpdateView):
    model = Menu_Item
    template_name = "update.html"
    success_url  = reverse_lazy('app_orders:Menu_ItemListView')
    fields = '__all__'


class Menu_ItemCreateView(CreateView):
    model = Menu_Item
    template_name = "create.html"
    success_url  = reverse_lazy('app_orders:Menu_ItemListView')
    fields = '__all__' 



################################################

class MenuListView(ListView):
    model = Menu
    template_name = "MenuListView.html"
    context_object_name = 'menu'


class MenuDeleteView(DeleteView):
    model = Menu
    template_name = "delete.html"
    success_url  = reverse_lazy('app_orders:MenuListView')
    

class MenuUpdateView(UpdateView):
    model = Menu
    template_name = "update.html"
    success_url  = reverse_lazy('app_orders:MenuListView')
    fields = '__all__' 



class MenuCreateView(CreateView):
    model = Menu
    template_name = "create.html"
    success_url  = reverse_lazy('app_orders:MenuListView')
    fields = '__all__' 



################################################

class TableListView(ListView):
    model = Table
    template_name = "TableListView.html"
    context_object_name = 'table'

class TableDeleteView(DeleteView):
    model = Table
    template_name = "delete.html"
    success_url  = reverse_lazy('app_orders:TableListView')

class TableUpdateView(UpdateView):
    model = Table
    template_name = "update.html"
    success_url  = reverse_lazy('app_orders:TableListView')
    fields = '__all__' 


class TableCreateView(CreateView):
    model = Table
    template_name = "create.html"
    success_url  = reverse_lazy('app_orders:TableListView')
    fields = '__all__' 



################################################

class oredr_itemListView(ListView):
    model = Order_Item
    template_name = "oredr_itemListView.html"
    context_object_name = 'oredr_item'


class oredr_itemDeleteView(DeleteView):
    model = Order_Item
    template_name = "delete.html"
    success_url  = reverse_lazy('app_orders:oredr_itemListView')

class oredr_itemUpdateView(UpdateView):
    model = Order_Item
    template_name = "update.html"
    success_url  = reverse_lazy('app_orders:oredr_itemListView')
    fields = '__all__' 



class oredr_itemCreateView(CreateView):
    model = Order_Item
    template_name = "create.html"
    success_url  = reverse_lazy('app_orders:oredr_itemListView')
    fields = '__all__' 



################################################

class orderListView(ListView):
    model = Order
    template_name = "orderListView.html"
    context_object_name = "order"

class orderDeleteView(DeleteView):
    model = Order
    template_name = "delete.html"
    success_url  = reverse_lazy('app_orders:orderListView')

class orderUpdateView(UpdateView):
    model = Order
    template_name = "update.html"
    success_url  = reverse_lazy('app_orders:orderListView')
    fields = '__all__' 



class orderCreateView(CreateView):
    model = Order
    template_name = "create.html"
    success_url  = reverse_lazy('app_orders:orderListView')
    fields = '__all__' 






