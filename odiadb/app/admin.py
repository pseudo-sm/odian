from django.contrib import admin
from . models import AllInfo
from admin_numeric_filter.admin import RangeNumericFilter, \
    SliderNumericFilter
# Register your models here.

class AdminAllInfo(admin.ModelAdmin):

    list_display=('business_code','person_name','product','contact_no','whatsapp_no','address')
    list_filter=('category','sub_category',('price',RangeNumericFilter),'contacted')
    search_fields=('business_code','person_name','product','contact_no','whatsapp_no','address')
admin.site.register(AllInfo,AdminAllInfo)
