from django.contrib import admin
from app1.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'age', 'created_at']
    search_fields = ['name', 'email']
    list_filter = ['age', 'created_at']
    ordering = ['id']

admin.site.register(Student, StudentAdmin)