from django.contrib import admin

# Register your models here.
from . models import Cat, Product

class catAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Cat,catAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','create','update']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)