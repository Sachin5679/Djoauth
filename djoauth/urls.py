from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('initiate_oauth/', views.initiate_oauth, name='initiate_oauth'),
    # path('oauth_callback/', views.oauth_callback, name='oauth_callback'), 
    path('', views.page, name='page'),
    path('welcome/', views.welcome_page, name='welcome_page'), 
    path('accounts/login/', views.oauth_callback, name='callback_page'),
]
