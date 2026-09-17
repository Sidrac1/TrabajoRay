from django.contrib import admin

from api import models

@admin.register(models.Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "timestamp",
        "status",
    ]

    