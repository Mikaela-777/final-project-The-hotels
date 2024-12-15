from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'reservation', 'amount', 'payment_date', 'payment_method', 'status', 'transaction_id')  # Kolom yang ditampilkan
    list_filter = ('payment_method', 'status', 'payment_date')  # Tambahkan filter untuk mempermudah pencarian
    search_fields = ('transaction_id', 'reservation__id')  # Pencarian berdasarkan ID transaksi dan ID reservasi
    ordering = ('-payment_date',)  # Urutkan berdasarkan tanggal pembayaran terbaru
    readonly_fields = ('payment_date',)  # Field yang hanya bisa dibaca (tidak bisa diedit)

    # Tambahkan tampilan thumbnail untuk bukti pembayaran (jika ada gambar)
    def proof_of_payment_preview(self, obj):
        if obj.proof_of_payment:
            return f'<img src="{obj.proof_of_payment.url}" style="max-height: 100px;"/>'
        return "No image available"
    proof_of_payment_preview.allow_tags = True
    proof_of_payment_preview.short_description = "Proof of Payment Preview"
