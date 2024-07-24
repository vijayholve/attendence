from django.urls import path 

urlpatterns = [
    path("login-page/",views.login_page,name="login-page"),
    path("logout-page/",views.logout_page,name="logout-page"),    
    path("register/",views.register,name="register"),
]
