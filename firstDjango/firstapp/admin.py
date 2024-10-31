from django.contrib import admin
from .models import User, UserReviw, UserCertificate, Store

# Register your models here.
class UserReviewInline(admin.TabularInline):
    model = UserReviw
    extra = 2
    fk_name = "user"
    
class UserType(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [UserReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('userType',)

class UserCertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'certificate_number')



admin.site.register(User, UserType)
admin.site.register(Store , StoreAdmin)
admin.site.register(UserCertificate , UserCertificateAdmin)

