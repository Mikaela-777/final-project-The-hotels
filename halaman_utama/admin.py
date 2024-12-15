from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone_number', 'address', 'age')  # Kolom yang ditampilkan di halaman admin
    search_fields = ('name', 'user__username', 'phone_number')  # Kolom yang dapat dicari
    list_filter = ('age',)  # Filter berdasarkan umur
    ordering = ('name',)  # Urutan berdasarkan nama
