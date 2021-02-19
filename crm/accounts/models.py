from django.db import models

# Create your models here.

class Info(models.Model):
	name = models.CharField(max_length=100, null=True)
	phone = models.CharField(max_length=150, null=True)
	email = models.CharField(max_length=150, null=True)
	adress = models.CharField(max_length=200, null=True)
	age = models.CharField(max_length=10, null=True)
	sex = models.CharField(max_length=50, null=True)
	talents = models.CharField(max_length=500, null=True)
	wishes = models.CharField(max_length=1000, null=True)


	def __str__(self):
		return str(self.name)















class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def orders(self):
		order_count = self.order_set.all().count()
		return str(order_count)
	


class Product(models.Model):

	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True) 
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.name



class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			) 

	customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return str(self.product)


