from django.contrib import admin
from .models import Phone, Apple, Digma, Vertex


@admin.register(Phone)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Apple)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Digma)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Vertex)
class PersonAdmin(admin.ModelAdmin):
    pass

