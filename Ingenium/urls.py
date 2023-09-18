from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("drama", views.drama, name="drama"),
    path("music", views.music, name="music"),
    path("literature", views.literature, name="literature"),
    path("art", views.art, name="art"),
    path("photography", views.photography, name="photography"),
    path("design", views.design, name="design"),
    path("media", views.media, name="media"),
    path("logistics", views.logistics, name="logistics"),
    path("hr", views.hr, name="hr"),
    path("pr", views.pr, name="pr"),
]
