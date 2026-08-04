from django.db import models
from blog.models import Category
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field


class Page(models.Model):

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    cover_image = models.ImageField(
            upload_to="Page/",
            blank=True,
            null=True
    )

    content = CKEditor5Field(
        "Content",
        config_name="extends"
    )

    meta_title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    meta_description = models.TextField(
        blank=True,
        null = True
    )

    is_published = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True)

    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class SiteSetting(models.Model):

    site_name = models.CharField(max_length=255)

    logo = models.ImageField(upload_to="site/")

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    address = models.TextField()

    def __str__(self):
        return self.site_name

class Menu(models.Model):

    title = models.CharField(max_length=100)

    url = models.CharField(max_length=100)

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    order = models.PositiveBigIntegerField(default=0)

    location = models.CharField(
        max_length=20,
        choices=[
            ("header", "Header"),
            ("footer", "Footer"),
        ],
        default="header",
    )

    target_blank = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.CharField(max_length=150)

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    subject = models.CharField(max_length=255)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject