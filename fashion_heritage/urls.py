from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gown/<int:gown_id>", views.gown_detail, name="gown_detail"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("like/<int:gown_id>", views.like_gown, name="like_gown"),
    path("save/<int:gown_id>", views.save_gown, name="save_gown"),
    path("saved_gowns/", views.saved_gowns, name="saved_gowns"),
    path("comment/<int:gown_id>", views.add_comment, name="add_comment"),
    path("search/", views.search, name="search"),
]