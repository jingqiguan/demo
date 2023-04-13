from django.contrib import admin

from .models import Node, Price, Transaction, Account

admin.site.register(Node)
admin.site.register(Price)
admin.site.register(Transaction)
admin.site.register(Account)
