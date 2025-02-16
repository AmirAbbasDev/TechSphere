from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="home"),
    path(
        "post/<int:id>/<slug:slug>/",
        views.article_detail_view,
        name="post-detail",
    ),
    path("create-post/", views.create_post_view, name="create-post"),
    path(
        "delete-comment/<int:comment_id>/", views.delete_comment_view, name="delete-comment"
    ),
]
