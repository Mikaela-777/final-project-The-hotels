from django.contrib import admin
from .models import Reservation
from django.utils.translation import gettext_lazy as _

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'check_in', 'check_out', 'status', 'payment_status')  # Kolom yang ditampilkan
    list_filter = ('status', 'payment_status', 'room')  # Filter berdasarkan status, payment status, dan room
    search_fields = ('user__username', 'room__room_number')  # Kolom yang bisa dicari
    ordering = ('-check_in',)  # Urutkan berdasarkan check_in (terbaru pertama)
    list_per_page = 20  # Batasi tampilan 20 entri per halaman
    
    # Menambahkan label yang lebih ramah pengguna
    fieldsets = (
        (None, {
            'fields': ('room', 'user')
        }),
        (_('Dates'), {
            'fields': ('check_in', 'check_out')
        }),
        (_('Reservation Status'), {
            'fields': ('status', 'payment_status')
        }),
    )

    # Menambahkan aksi khusus di admin
    actions = ['mark_as_completed', 'mark_as_cancelled']

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
        self.message_user(request, _("The selected reservations have been marked as completed."))

    def mark_as_cancelled(self, request, queryset):
        queryset.update(status='cancelled')
        self.message_user(request, _("The selected reservations have been marked as cancelled."))

    mark_as_completed.short_description = _('Mark selected as completed')
    mark_as_cancelled.short_description = _('Mark selected as cancelled')


# Register Reservation model with custom admin configuration
admin.site.register(Reservation, ReservationAdmin)
