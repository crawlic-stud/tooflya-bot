from django.contrib import admin

from .models import Product, ProductImage, TelegramUser


class InlineProductImage(admin.TabularInline):
    model = ProductImage
    readonly_fields = ("image_preview",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        InlineProductImage,
    ]


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    pass
