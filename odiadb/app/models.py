from django.db import models

# Create your models here.


class Product(models.Model):
    product = models.CharField(max_length=255,null=True,blank=True)
    category = models.CharField(max_length=255,null=True,blank=True)
    sub_category = models.CharField(max_length=255,null=True,blank=True)
    details = models.CharField(max_length=255,null=True,blank=True)
    price = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.product
    


class Business(models.Model):

    business_code = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=255,null=True,blank=True)
    suppliers = models.CharField(max_length=255,null=True,blank=True)
    contact_no = models.CharField(max_length=255,null=True,blank=True)
    whatsapp_no = models.CharField(max_length=255,null=True,blank=True)
    email_id = models.CharField(max_length=255,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    contacted = models.BooleanField(default=False)

    def __str__(self):
        return self.person_name

class BusinessProduct(models.Model):

    business = models.ForeignKey(Business,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="images/", max_length=100)
    product = models.ForeignKey(Product,null=True,blank=True,on_delete=models.CASCADE)
