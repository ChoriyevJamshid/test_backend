from django.contrib import admin

from django.apps import apps
from . import models


# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')


@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('product', 'material', 'quantity')


@admin.register(models.Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('material', 'remainder', 'price')
