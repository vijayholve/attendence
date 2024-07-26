from django.urls import path 
from . import views
urlpatterns = [
    path("login-page/",views.customize_login_page,name="login-page"),
    path("logout-page/",views.logout_page,name="logout-page"),    
    path("register/",views.customeze_register_page,name="register"),
    path('user-type/<str:user_id>/<str:user_type>/',views.user_panel,name="user-type"),
]
