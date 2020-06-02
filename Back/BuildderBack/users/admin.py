from django.contrib import admin

# Register your models here.

from .models import B_User

class UserModelAdmin(admin.ModelAdmin):

    list_display = ["first_name","last_name","joined","password"]

    list_filter = ["joined"]

    search_fields=["first_name","last_name"]

    class Meta:
        model = B_User

admin.site.register(B_User,UserModelAdmin)