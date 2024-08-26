from django.contrib import admin
from .models import Address
from django.contrib.auth.models import User



class AddressInline(admin.StackedInline):
    model = Address


admin.site.unregister(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (AddressInline, )
    readonly_fields = ('password',)

