from django.db import models

# Create your models here.

class AllInfo(models.Model):

    business_code = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=255,null=True,blank=True)
    product = models.CharField(max_length=255,null=True,blank=True)
    category = models.CharField(max_length=255,null=True,blank=True)
    sub_category = models.CharField(max_length=255,null=True,blank=True)
    details = models.CharField(max_length=255,null=True,blank=True)
    price = models.FloatField(null=True,blank=True)
    suppliers = models.CharField(max_length=255,null=True,blank=True)
    contact_no = models.CharField(max_length=255,null=True,blank=True)
    whatsapp_no = models.CharField(max_length=255,null=True,blank=True)
    email_id = models.CharField(max_length=255,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    contacted = models.BooleanField(default=False)

class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="images/", max_length=100)
    row_id = models.ForeignKey(AllInfo,null=True,blank=True,on_delete=models.CASCADE)
