from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('client_info/<int:pk>', views.client_info, name='client_info'),
    path('delete/<int:pk>', views.delete_client, name='delete_client'),
    path('add_client/', views.add_client, name='add_client'),
    path('update_client_info/<int:pk>', views.update_client_info, name='update_client_info'),
]
