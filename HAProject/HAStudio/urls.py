from django.urls import path
from HAStudio import views


urlpatterns = [
    path('send_telegram', views.send_post_to_telegram_view, name='send_telegram'),
    path('logged_out', views.user_logout, name='logged_out'),
    path('reg_auth', views.reg_auth, name='reg_auth'),
    path('service_response', views.service_response, name='service_response'),
    path('user/registration', views.registration, name='registration'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('posts', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
    path('', views.index, name='index'),
]


# path('login/', views.user_login, name='login'),
# path('logout', views.logout, name='logout'),
# path('logout', 'django.contrib.auth.views.logout', name='logout'),
# path('login', 'django.contrib.auth.views.login', name='login'),
# path('logout-then-login', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),