from django.urls import path

from . import views # used . because they are in same folder


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>",views.greet,name="greet"),  # here <str:name> will take parameter form url and send that to views page
    path("dinesh",views.dinesh, name="dinesh"),
    path("umesh",views.umesh, name="umesh"),
]
