from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("",views.home,name="home"),
] 
if settings.DEBUG:  
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root =settings.MEDIA_ROOT)
