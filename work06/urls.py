from django.urls import path


from . import views

urlpatterns = [
    path("reiwa/", views.index, name="reiwa"),
]
