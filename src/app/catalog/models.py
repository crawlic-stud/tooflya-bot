from django.db import models
from django.utils.safestring import mark_safe

from .services.image_processing import optimize_and_save_image


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.SmallIntegerField()

    def __str__(self):
        return f"{self.name} {self.price} руб. ({self.in_stock})"


class CompressedImageField(models.ImageField):
    def pre_save(self, instance: "CompressedImageField", add: bool):
        new_image_url = optimize_and_save_image(
            instance.image.file.file, instance.image.file.name
        )
        instance.image.name = new_image_url
        return instance.image


class ProductImage(models.Model):
    image = CompressedImageField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )

    @property
    def image_url(self) -> str:
        return "/" + str(self.image)

    @property
    def image_preview(self) -> str:
        if self.image:
            return mark_safe(
                f'<img src="{self.image_url}" max-height="200" style="object-fit: cover;" />'
            )
        else:
            return "(No image)"


class TelegramUser(models.Model):
    telegram_id = models.IntegerField()
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    username = models.TextField(null=True)
    language_code = models.TextField(null=True)

    favorites = models.ManyToManyField(Product, related_name="users")

    def __str__(self):
        return f"{self.first_name} {self.last_name} (@{self.username})"
