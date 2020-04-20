from django.urls import path,include
from home_app import views

app_name = 'baseapp'
urlpatterns = [
    path('reg/',views.register,name='hello'),
    path('user_login/',views.user_login,name='user_login'),
]
