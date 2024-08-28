from django.contrib import admin

from .models import Product, ProductImage


class InlineProductImage(admin.TabularInline):
    model = ProductImage
    readonly_fields = ("image_preview",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        InlineProductImage,
    ]
