from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at')  # Kolom yang ditampilkan di halaman admin
    search_fields = ('user__username', 'message')  # Pencarian berdasarkan username pengguna dan pesan
    list_filter = ('created_at',)  # Filter berdasarkan tanggal
    ordering = ('-created_at',)  # Urutkan berdasarkan tanggal terbaru
    readonly_fields = ('created_at',)  # Buat kolom created_at menjadi readonly

