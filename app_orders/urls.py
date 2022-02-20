from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name= "app_orders"
urlpatterns = [
    path("our_menu/<int:pk>/",OurMenu.as_view(),name="our_menu" ),      
          
    path("our_menu/<int:pk>/<str:status>/<int:order_id>/",OurMenu.as_view(),name="our_menu_after" ),                

    path("our_menu/add_order/", AddOrder.as_view(), name="add_order" ),
    # ليس لها تمبلت

    path("our_menu/checkout/<int:pk>/", Checkout.as_view(), name="checkout" ),

    path('our_menu/delete_order_item/<int:pk>/', DeleteOrderItem.as_view(), name="delete_order_item" ),
   
    path('our_menu/<int:pk>/confirm_order_by_user/', ConfirmOrderByUser.as_view(), name="confirm_order_by_user" ),
     # ليس لها تمبلت

    path('our_menu/YesWaiterConfirmedOrder-DeliveredOrder/', login_required( YesWaiterConfirmedOrderDeliveredOrder.as_view()), name="YesWaiterConfirmedOrderDeliveredOrder" ),

    path('our_menu/YesChefCookedOrder_kitchen1/', login_required( YesChefCookedOrder_kitchen1.as_view()), name="YesChefCookedOrder_kitchen1" ),
    path('our_menu/YesChefCookedOrder_kitchen2/', login_required( YesChefCookedOrder_kitchen2.as_view()), name="YesChefCookedOrder_kitchen2" ),
    path('our_menu/YesChefCookedOrder_kitchen3/', login_required( YesChefCookedOrder_kitchen3.as_view()), name="YesChefCookedOrder_kitchen3" ),
    
    path('our_menu/YesCashierOrder/', login_required( YesCashierOrder.as_view()), name="YesCashierOrder" ),

    path('our_menu/HasCashierPrintOrder/<int:pk>', login_required( HasCashierPrintOrder.as_view()), name="HasCashierPrintOrder" ),

    path('our_menu/<int:pk>/ConfirmPaidByCashier/', ConfirmPaidByCashier.as_view(), name="ConfirmPaidByCashier" ),


    path('our_menu/HasWaiterConfirmedOrder/<int:pk>/', login_required( HasWaiterConfirmedOrder.as_view()), name="HasWaiterConfirmedOrder" ),

    path('our_menu/HasWaiterDeliveredOrder/<int:pk>/', login_required( HasWaiterDeliveredOrder.as_view()), name="HasWaiterDeliveredOrder" ),
                  
    path('our_menu/HasChefCookedOrder/<int:pk>/',login_required(  HasChefCookedOrder.as_view()), name="HasChefCookedOrder" ),

    path("our_menu/OrderDetails/<int:pk>/", OrderDetails.as_view(), name="OrderDetails" ),





    path("manger/Menu_ItemListView" , login_required(   Menu_ItemListView.as_view() ), name="Menu_ItemListView" ),
    path("manger/Menu_ItemDeleteView/<int:pk>/" , login_required(   Menu_ItemDeleteView.as_view() ), name="Menu_ItemDeleteView" ),
    path("manger/Menu_ItemUpdateView/<int:pk>/" , login_required(   Menu_ItemUpdateView.as_view() ), name="Menu_ItemUpdateView" ),
    path("manger/Menu_ItemCreateView/" , login_required(   Menu_ItemCreateView.as_view() ), name="Menu_ItemCreateView" ),

    path("manger/MenuListView" , login_required(   MenuListView.as_view() ) , name="MenuListView" ),
    path("manger/MenuDeleteView/<int:pk>/" , login_required(   MenuDeleteView.as_view() ), name="MenuDeleteView" ),
    path("manger/MenuUpdateView/<int:pk>/" , login_required(   MenuUpdateView.as_view() ), name="MenuUpdateView" ),
    path("manger/MenuCreateView/" , login_required(  MenuCreateView.as_view() ), name="MenuCreateView" ),


    path("manger/TableListView" , login_required(  TableListView.as_view() ) , name="TableListView" ),
    path("manger/TableDeleteView/<int:pk>/" , login_required(  TableDeleteView.as_view() ), name="TableDeleteView" ),
    path("manger/TableUpdateView/<int:pk>/" ,login_required(  TableUpdateView.as_view() ), name="TableUpdateView" ),
    path("manger/TableCreateView/" , login_required(  TableCreateView.as_view() ), name="TableCreateView" ),


    path("manger/oredr_itemListView" , login_required(  oredr_itemListView.as_view() ), name="oredr_itemListView" ),
    path("manger/oredr_itemDeleteView/<int:pk>/" ,login_required(   oredr_itemDeleteView.as_view() ), name="oredr_itemDeleteView" ),
    path("manger/oredr_itemUpdateView/<int:pk>/" , login_required(  oredr_itemUpdateView.as_view() ), name="oredr_itemUpdateView" ),
    path("manger/oredr_itemCreateView/" ,login_required(  oredr_itemCreateView.as_view() ), name="oredr_itemCreateView" ),

    path("manger/orderListView" , login_required(  orderListView.as_view() ), name="orderListView" ),
    path("manger/orderDeleteView/<int:pk>/" , login_required(  orderDeleteView.as_view() ), name="orderDeleteView" ),
    path("manger/orderUpdateView/<int:pk>/" , login_required(  orderUpdateView.as_view() ), name="orderUpdateView" ),
    path("manger/orderCreateView/" , login_required( orderCreateView.as_view() ), name="orderCreateView" ),




]                         

