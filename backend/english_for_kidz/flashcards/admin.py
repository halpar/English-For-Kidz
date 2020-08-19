from django.contrib import admin

# Register your models here.

from .models import Card,CardCategory,User


admin.site.register(Card)
admin.site.register(CardCategory)
admin.site.register(User)
