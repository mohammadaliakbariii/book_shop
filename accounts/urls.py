from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('signup/',views.sign_up,name='sign_up'),
    path('login/',views.login_customer,name='login_customer'),
    path('login/', views.login_staff, name='login_staff'),
    path('logout/', views.logOut, name='logout'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
]