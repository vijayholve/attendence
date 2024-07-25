from django.urls import path 
from . import views
urlpatterns = [
    path("login-page/",views.login_page,name="login-page"),
    path("logout-page/",views.logout_page,name="logout-page"),    
    path("register/",views.register_page,name="register"),
    path('user-type/<str:pk>/',views.user_type,name="")
]
