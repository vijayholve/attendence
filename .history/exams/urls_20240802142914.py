from django.urls import path
from . import views


urlpatterns = [
    path('exam-create',views.ExamsForm,),
]



