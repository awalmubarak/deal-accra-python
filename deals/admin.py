from django.contrib import admin
from django.forms import TextInput, Textarea
from .models import Deal
from django.db import models


class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '80'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 80})},
    }


admin.site.register(Deal, YourModelAdmin)
