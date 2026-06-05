from django.contrib import admin
from about_us.models import About_us,Partner

# Register your models here.
class About_usAdmin(admin.ModelAdmin):
    list_display = ('development_history_time','development_history_content')

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    
admin.site.register(About_us,About_usAdmin)
admin.site.register(Partner,PartnerAdmin)
