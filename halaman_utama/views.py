from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from halaman_utama.forms import CreateUserForm
import logging
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserUpdateForm, CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash

logger = logging.getLogger(__name__)
# Create your views here.
def home(request):
    logger.info("Home view accessed")
    return render(request, 'home.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {form.cleaned_data["username"]}')

            return redirect('home')

    context = {'form' :form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password incorrect')

    context = {}
    return render(request, 'home.html', context)

def profilePage(request):
    if not request.user.is_authenticated:
        messages.info(request, "You need to log in to view your profile.")
        return redirect('login')

    # Ambil profil pengguna yang sedang login (dari UserProfile)
    profile = UserProfile.objects.filter(user=request.user).first()

    context = {
        'user': request.user,
        'profile': profile  # Tambahkan profil pengguna ke context
    }
    return render(request, 'accounts/profile.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')


@login_required
def profile_view(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    context = {
        'user': request.user,
        'profile': profile
    }
    return render(request, 'accounts/profile.html', context)


def edit_user_profile(request):
    try:
        # Coba ambil profil yang sudah ada
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Jika tidak ada, buat objek UserProfile baru untuk user yang sedang login
        profile = UserProfile(user=request.user)

    # Proses form
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Ganti dengan URL tujuan setelah profil disimpan
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def update_user_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        
        if user_form.is_valid() and password_form.is_valid():
            # Simpan perubahan username dan email
            user_form.save()
            # Simpan perubahan password
            password_form.save()
            # Perbarui sesi pengguna
            update_session_auth_hash(request, password_form.user)
            
            messages.success(request, 'Profil berhasil diperbarui!')
            return redirect('update_profile')
        else:
            messages.error(request, 'Terjadi kesalahan. Silakan periksa form Anda.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)
    
    return render(request, 'accounts/change_pasword.html', {
        'user_form': user_form,
        'password_form': password_form,
    })