from typing import Callable
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Menu (Category)

# class Category(models.Model):
#     created_by = models.ForeignKey(User,on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)

# class MenuItem(models.Model):

#     kitchen_CHOICES = (
#         ('kitchen 1', 'drinks'),
#         ('kitchen 2', 'arabic food'),
#         ('kitchen 3', 'western food'),
#     )

#     # Relations
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)

#     # menu information
#     name = models.CharField(max_length=20,null=True,blank=True)
#     price = models.DecimalField( max_digits=5, decimal_places=2, null=True , blank=True)
#     description = models.TextField(max_length=200)
#     image  = models.ImageField(null=True,blank=True)
#     slug = models.SlugField(null=True,blank=True)
#     available = models.BooleanField(default=True)
#     kitchen_type = models.CharField(max_length=50,choices=kitchen_CHOICES , null=True)




class Menu_Item(models.Model):
    kitchen_CHOICES = (
        ('kitchen 1', 'drinks'),
        ('kitchen 2', 'arabic food'),
        ('kitchen 3', 'western food'),
    )

    category_CHOICES = (
        ('category1', 'pizza'),
        ('category2', 'steak'),
        ('category3', 'burger'),
        ('category4', 'juice'),
        ('category5', 'rice'),
        ('category6', 'pasta'),
    )
    #category = models.ForeignKey("Çategory",on_delete=models.CASCADE)
    name = models.CharField(max_length=20,null=True,blank=True)
    price = models.DecimalField( max_digits=5, decimal_places=2, null=True , blank=True)
    description = models.TextField(max_length=200)
    image  = models.ImageField(null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    available = models.BooleanField(default=True)
    kitchen_type = models.CharField(max_length=50,choices=kitchen_CHOICES , null=True)
    category_type =  models.CharField(max_length=50,choices=category_CHOICES , null=True)
    




    # settings.AUTH_USER_Model استخدام كلمة يوزر فقط أفضل من استخدام الجملة 

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self): return reverse("app_orders:...._model_detail", args=[self.pk])
    # لم نستخدم الدالة السابقة بتاتا في صفحة المودلز لأننا في مشروعنا الحالي لم نعمل في صفحة الفيوز كلاس ل الديتيلز .. و الدالة السابقة تخصصها فقط في كلاسات الديتيلز من صفحة الفيوز


    class Meta:
        verbose_name=' Menu_Item'
        verbose_name_plural=' Menu_Items'



class Menu(models.Model):
    menu_name = models.CharField( max_length=50 , null=True)
    menu_items = models.ManyToManyField(Menu_Item, related_name='menu_items',verbose_name='menu_items' )
        # الفيربس نيم في السطر السابق ليست خاصة بصفحة الأدمن بانل (مثلما كنا نعمل في كلاس الميتا)بل خاصة باسم العلاقة بين السطر السابق و ... من قواعد البيانات ربما سوف تلزمك لاحقا

    
    def __str__(self):
        return self.menu_name

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"

    def return_choices_values(self):
        x =  Menu_Item.category_CHOICES
        foo = [y[1] for y in x ]
        print(foo)
        return foo


    # def return_choices_keys(self):
    #     x =  Menu_Item.category_CHOICES
    #     foo = [y[1] for y in x ]
    #     print(foo)
    #     return foo


class Table(models.Model):
    Table_Menu = models.ForeignKey( Menu , related_name='Table_Menu', on_delete=models.CASCADE , default=None , null=True , blank=True )
    number = models.IntegerField( validators=[MaxValueValidator(10),MinValueValidator(1)] , unique=True)
   
    def __str__(self):
        return 'table ' + str(self.number) 


    class Meta:
        verbose_name='Table'
        verbose_name_plural='Table'


class Order_Item(models.Model):
    
    TRUE_FALSE_CHOICES = ( (True, 'Yes'),(False, 'No'))

    food_item = models.ForeignKey(Menu_Item, verbose_name='food_item' , on_delete=models.SET_NULL , null=True)
        # الفيربس نيم في السطر السابق ليست خاصة بصفحة الأدمن بانل (مثلما كنا نعمل في كلاس الميتا)بل خاصة باسم العلاقة بين السطر السابق و ... من قواعد البيانات ربما سوف تلزمك لاحقا
#  اسخدمنا السيت نال و ليس الكاسكيد لأن في حالة السيت نال اذا تم حذف طعام معين من الأوردر فان ذلك الطعام يبقى موجود في باقي الأوردرات و لكن في حالة الكاس كيد فان ذلك الطعام سيتم حذفه من جميع الأوردرات الأخرى و هذا غير منطقي 
    count = models.IntegerField()

    has_confirmed_by_cheif = models.BooleanField(default=False , null=True ,choices = TRUE_FALSE_CHOICES,)
    has_been_delivered = models.BooleanField(default=False , null=True ,choices = TRUE_FALSE_CHOICES,)
    time =  models.DateTimeField( auto_now_add=True , null=True)


    def __str__(self):
        return f'{self.food_item} | {self.count}'


    class Meta:
        verbose_name='order_item'
        verbose_name_plural='order_item'
    

class Order(models.Model):
    TRUE_FALSE_CHOICES = ( (True, 'Yes'),(False, 'No'))
    order_food_item = models.ManyToManyField(Order_Item, verbose_name='order_food_item ')
        # الفيربس نيم في السطر السابق ليست خاصة بصفحة الأدمن بانل (مثلما كنا نعمل في كلاس الميتا)بل خاصة باسم العلاقة بين السطر السابق و ... من قواعد البيانات ربما سوف تلزمك لاحقا

    time =  models.DateTimeField( auto_now_add=True , null=True)
    table = models.ForeignKey(Table, verbose_name='table', on_delete=models.CASCADE)
    # الفيربس نيم في السطر السابق ليست خاصة بصفحة الأدمن بانل (مثلما كنا نعمل في كلاس الميتا)بل خاصة باسم العلاقة بين السطر السابق و ... من قواعد البيانات ربما سوف تلزمك لاحقا
    has_confirmed_by_user = models.BooleanField(default=False , null=True ,choices = TRUE_FALSE_CHOICES,)
    has_confirmed_by_waiter = models.BooleanField(default=False , null=True ,choices = TRUE_FALSE_CHOICES,)

    has_been_paid = models.BooleanField(default=False , null=True ,choices = TRUE_FALSE_CHOICES,)



    def __str__(self):
        return f'order of {self.table} '


    class Meta:
        verbose_name = "order"
        verbose_name_plural = "order"
 





class materials(models.Model):
    
    status_CHOICES = (
        ('1', 'available'),
        ('2', ' come to finished '),
        ('3', ' finished'),
    )
    
    name = models.CharField( max_length=50)
    status = models.CharField(max_length=50,choices=status_CHOICES , null=True)

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materials'

    def __str__(self):
        return self.name

