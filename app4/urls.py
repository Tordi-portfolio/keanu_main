# store/urls.py
from django.urls import path
from . import views
from .views import change_username, change_password
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('product_list', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('sell', views.sell, name='sell'),
    path('change_username/', change_username, name='change_username'),
    path('change_password/', change_password, name='change_password'),
    path('settings', views.settings, name='settings'),
    path('change_email/', views.change_email, name='change_email'),
    path('update_profile-picture/', views.update_profile_picture, name='update_profile_picture'),
    path('delete_account/', views.delete_account, name='delete_account'),

    # Forgot password (Step 1: request reset email)
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='app4/password_reset.html'), name='reset_password'),

    # Step 2: email sent confirmation
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='app4/password_reset_sent.html'), name='password_reset_done'),

    # Step 3: link from email
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app4/password_reset_confirm.html'), name='password_reset_confirm'),

    # Step 4: password successfully changed
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app4/password_reset_complete.html'), name='password_reset_complete'),
]