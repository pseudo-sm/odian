from django.contrib import admin
from . models import Business,Product,File,BusinessProduct
from admin_numeric_filter.admin import RangeNumericFilter, \
    SliderNumericFilter
# Register your models here.

class AdminMedia(admin.TabularInline):
    model = File


class AdminBusinessProduct(admin.ModelAdmin):
    list_display=('get_product_name','get_product_category','get_product_price','get_product_subcategory','get_businesses')
    search_fields=('product__product_name','business__business_code','product__category','product__sub_category','business__business_code')
    list_filter=('product__category','product__sub_category',('product__price',RangeNumericFilter),'product__product_name','business__business_name')[::-1]
    @admin.display(description='Product', ordering='product__product_name')
    def get_product_name(self, obj):
        return obj.product.product_name

    @admin.display(description='Category', ordering='product__category')
    def get_product_category(self, obj):
        return obj.product.category
    
    @admin.display(description='Price', ordering='product__price')
    def get_product_price(self, obj):
        return obj.product.price
    
    @admin.display(description='Sub Category', ordering='product__sub_category')
    def get_product_subcategory(self, obj):
        return obj.product.sub_category
    
    @admin.display(description='Businesses')
    def get_businesses(self, obj):
        result = ",".join([p.business_name for p in Business.objects.filter(business_code=obj.business.business_code)])
        return result

admin.site.register(Business)
admin.site.register(Product)
admin.site.register(BusinessProduct,AdminBusinessProduct)