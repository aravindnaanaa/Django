from django.urls import path
from . import views

urlpatterns = [
 path("", views.index, name="index"),
 path("naanaa", views.naanaa, name="naanaa"),
 path("<str:name>", views.greetings,name="greetings")
]