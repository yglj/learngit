from django.contrib import admin
from booktest.models import Book, Role

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'bname', 'pub_date']


admin.site.register(Book, BookAdmin)
admin.site.register(Role)
