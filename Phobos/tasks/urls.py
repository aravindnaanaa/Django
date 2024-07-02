from django.urls import path
from. import views

app_name = "tasks"
urlpatterns = [
 path("", views.index, name="inde"),
 path("add", views.add, name="add")
]
