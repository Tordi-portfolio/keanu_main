from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('chat/', views.chat_with_admin, name='chat_with_admin'),
    path('dashboard/users/', views.admin_user_list, name='admin_user_list'),
    path('dashboard/chat/<int:user_id>/', views.admin_chat_view, name='admin_chat_view'),

    path('get-new-messages/', views.get_new_messages, name='get_new_messages'),
    path('get-unread-count/', views.get_unread_count, name='get_unread_count'),

    path('moodley/', views.moodley, name='moodley'),
    path('tamara/', views.tamara, name='tamara'),
    path('johnna/', views.johnna, name='johnna'),
    path('martha/', views.martha, name='martha'),
    path('fanspage/', views.fanspage, name='fanspage'),
    path('madelena', views.madelena, name='madelena'),
    path('lucie', views.lucie, name='lucie'),
]
