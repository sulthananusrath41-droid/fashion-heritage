from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from rest_framework.authtoken.views import obtain_auth_token
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
    path("api/gowns/", views.gown_list_api, name="gown_list_api"),
    path("api/gowns/<int:gown_id>/", views.gown_detail_api, name="gown_detail_api"),
    path('api/register/', views.register_api, name='register_api'),
    path('api/login/', obtain_auth_token, name='login_api'),
    path('api/gowns/<int:gown_id>/like/', views.like_gown_api, name='like_gown_api'),
    path('api/gowns/<int:gown_id>/save/', views.save_gown_api, name='save_gown_api'),
    path('api/gowns/<int:gown_id>/comment/', views.add_comment_api, name='add_comment_api'),
    path('api/saved-gowns/', views.saved_gowns_api, name='saved_gowns_api'),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]


