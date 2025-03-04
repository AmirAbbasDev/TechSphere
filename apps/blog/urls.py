from django.urls import path
from . import views
from .views import profile_view, edit_profile_view

urlpatterns = [
    path("", views.PostListView.as_view(), name="home"),
    path(
        'tag/<slug:tag_slug>/', views.PostListView.as_view(), name='post_list_by_tag'
    ),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.article_detail_view,
        name="post-detail",
    ),
    path("create-post/", views.create_post_view, name="create-post"),
    path(
        "create-comment/<int:post_id>",
        views.add_comment_to_post_view,
        name="create-comment",
    ),
    path(
        "delete-comment/<int:comment_id>/",
        views.delete_comment_view,
        name="delete-comment",
    ),
    path(
        "update-comment/<int:comment_id>",
        views.comment_update_view,
        name="update-comment",
    ),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path("<int:post_id>/share/", views.post_share_view, name="post-share"),
]
