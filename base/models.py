from operator import truediv
from django.db import models
from django.contrib.auth.models import User


# Create your models here...


## Category models
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'


'''  21.04.2022
## Subcategory models
class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'


# Sub subcategory models
class Subsubcategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.subcategory.category.slug}/{self.subcategory.slug}/{self.slug}/'


# Sub sub subcategory models
class Subsubsubcategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    subsubcategory = models.ForeignKey(Subsubcategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.subsubcategory.subcategory.category.slug}/{self.subsubcategory.subcategory.slug}/{self.subsubcategory.slug}/{self.slug}/'
        


## Product models
class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    subsubcategory = models.ForeignKey(Subsubcategory, on_delete=models.CASCADE)
    subsubsubcategory = models.ForeignKey(Subsubsubcategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.subcategory.slug}/{self.slug}/'
'''






class Product(models.Model):
    ### user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    vendor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    name = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) #category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')    #models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default='Default-Category')
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')
    brand = models.CharField(max_length=200, null=True, blank=True)

    #### category = models.CharField(max_length=200, null=True, blank=True)   ##this category is the old one
    
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    ### price = models.IntegerField(null=True, blank=True, default=0)

    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    ### id = models.AutoField(primary_key=True, editable=False) 
    ### objects = models.Manager()


    def __str__(self):
        return self.name






class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    # id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)

    
# class Review(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     rating = models.IntegerField(null=True, blank=True, default=0)
#     comment = models.TextField(null=True, blank=True)
#     createdAt = models.DateTimeField(auto_now_add=True)
#     #id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.rating)




'''   11/4/2022   no need for Cart  
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carts')
    quantity = models.IntegerField(default=1)
    createdAt = models.DateTimeField(auto_now_add=True)
    #id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.quantity)       
'''   
   
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    #_id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)





class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # text for vendor test
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    #_id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    #_id = models.AutoField(primary_key=True, editable=False) 

    def __str__(self):
        return str(self.address)




'''     test for vendor  
class Vendor(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    #_id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
'''


'''  
class Seller(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
'''


'''
# old Product model - works perfectly

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    #_id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name
'''