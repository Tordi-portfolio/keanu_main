# store/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    selected_category = request.GET.get('category')
    if selected_category:
        products = Product.objects.filter(category=selected_category)
    else:
        products = Product.objects.all()
    return render(request, 'product_list.html', {
        'products': products,
        'selected_category': selected_category
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def sell(request):
    return render(request, 'sell.html')



from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UsernameChangeForm, CustomPasswordChangeForm

@login_required
def change_username(request):
    if request.method == 'POST':
        form = UsernameChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Username updated successfully.")
            return redirect('change_username')
    else:
        form = UsernameChangeForm(instance=request.user)
    return render(request, 'change_username.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keeps user logged in
            messages.success(request, "Password updated successfully.")
            return redirect('change_password')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


def settings(request):
    return render(request, 'settings.html')


from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EmailChangeForm, ProfilePictureForm
from django.contrib.auth import logout

@login_required
def settings_view(request):
    return render(request, 'settings.html')

@login_required
def change_email(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Email updated.")
            return redirect('change_email')
    else:
        form = EmailChangeForm(instance=request.user)
    return render(request, 'change_email.html', {'form': form})

@login_required
def update_profile_picture(request):
    profile = request.user.profile  # assumes you have a Profile model with OneToOne
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile picture updated.")
            return redirect('update_profile_picture')
    else:
        form = ProfilePictureForm(instance=profile)
    return render(request, 'update_profile_picture.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, "Your account has been deleted.")
        logout(request)
        return redirect('home')  # or login page
    return render(request, 'delete_account.html')

