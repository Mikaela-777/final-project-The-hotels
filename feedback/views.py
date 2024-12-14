from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def submit_feedback(request):
    if request.method == "POST":
        message = request.POST.get("message")
        if message:
            Feedback.objects.create(user=request.user, message=message)
            messages.success(request, "Feedback berhasil dikirim!")
            return redirect("submit_feedback")
        else:
            messages.error(request, "Pesan tidak boleh kosong.")
    return render(request, "feedback/feedback.html")

@login_required
def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by("-created_at")  # Mengambil semua feedback, urut berdasarkan waktu
    return render(request, "feedback/feedback_list.html", {"feedbacks": feedbacks})