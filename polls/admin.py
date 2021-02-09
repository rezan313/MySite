from django.contrib import admin
from . import models
class ChoiceInline(admin.TabularInline):
    model=models.Choice
    extra = 1
@admin.register(models.Qustion)
class QustionAdmin(admin.ModelAdmin):
    model=models.Qustion
    inlines = [ChoiceInline]


# Register your models here.
