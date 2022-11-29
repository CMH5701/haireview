from django.contrib import admin

from .models import Review, R_comment

# Register your models here.

admin.site.register(Review)
admin.site.register(R_comment)

