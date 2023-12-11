from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("post/",views.post,name="post"),
    path("delete/<int:id>",views.delete,name="delete")
]