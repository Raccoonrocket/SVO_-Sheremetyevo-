from django.urls import path, include

from users import views
from users.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
    path('index/', views.index, name='index'),
]