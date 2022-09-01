import os
import django
import sys

sys.path.append('D:\\OdiaDb\\odiadb')
os.environ['DJANGO_SETTINGS_MODULE'] = 'odiadb.settings'
django.setup()


import pandas as pd
from app.models import Business,Product,BusinessProduct


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "odiadb.settings")
import django
django.setup()




def load_business(file_path):

    data = pd.read_csv(file_path)
    for _,row in data.iterrows():
        vendor_code = row["vendor_code"]
        vendor_name = row["vendor_name"]
        is_validated = row["is_validated"]
        contact_details = row["contact_details"]
        whatsapp = row["whatsapp"]
        organization_name = row["organization_name"]
        supplier_type = row["supplier_type"]
        address = row["address"]
        district = row["district"]
        feedback = row["feedback"]
        email_id = row["email_id"]
        new_business = Business(business_code = vendor_code,person_name=vendor_name,contact_no=contact_details,
                            whatsapp_no = whatsapp, business_name = organization_name,
                            supplier_type = supplier_type,
                            address = address, district = district, email_id = email_id,
                            is_validated = True
                        )
        new_business.save()

def load_products(file_path):
    data = pd.read_csv(file_path)
    for _,row in data.iterrows():
        product_code = row["product_code"]
        product_name = row["product_name"]
        category = row["category"]
        sub_category = row["sub_category"]
        product_description = row["product_description"]
        size = row["size"]
        weight = row["weight"]
        price = row["price"]
        new_product = Product(product_code=product_code,product_name=product_name,
                                category=category,sub_category=sub_category,
                                product_description=product_description,
                                size = size,weight=weight,
                                price = price
                                )
        new_product.save()

def map_business_product(file_path):

    data = pd.read_csv(file_path)
    for _,row in data.iterrows():
        product_code = row["product_code"]
        vendor_code = row["vendor_code"]
        product = Product.objects.get(product_code=product_code)
        business = Business.objects.get(business_code=vendor_code)
        new_mapping = BusinessProduct(product=product,business=business)
        new_mapping.save()

load_business(file_path="C:\\Users\\Lenovo\\Downloads\\vendors.csv")
load_products(file_path="C:\\Users\\Lenovo\\Downloads\\products.csv")
map_business_product(file_path="C:\\Users\\Lenovo\\Downloads\\mapping.csv")