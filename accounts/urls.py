from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('delete/', views.delete_user, name='delete_account'),
    path('change_password', views.change_password, name='change_password'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}',
         views.activate, name='activate')
]