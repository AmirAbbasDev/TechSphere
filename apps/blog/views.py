import re

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView

from blog.forms import CommentForm, PostForm

from .models import Comment, Post


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 9
    queryset = Post.published.all()


@login_required
def create_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            generate_slug_from_title(form, post)
            post.author = request.user
            post.save()
            return redirect(reverse("home"))
    else:
        form = PostForm()
    context = {"form": form}
    return render(request, "blog/create_post.html", context)


def generate_slug_from_title(form, post):
    slug = re.sub(r"[^\w\s-]", "", form.cleaned_data["title"])
    slug = re.sub(r"\s+", "-", slug)
    post.slug = slug.lower()


def article_detail_view(request, id, slug):
    post = get_object_or_404(Post, id=id)
    form = CommentForm()
    comments = Comment.objects.filter(post=post)
    add_comment_to_post(request, post)
    context = {
        "form": form,
        "comments": comments,
        "post": post,
    }
    return render(request, "blog/post_detail.html", context)


def add_comment_to_post(request, post):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(reverse("login"))
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(
                "post-detail", id=post.id, slug=post.slug
            )


@login_required
def delete_comment_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.user or request.user.is_staff:
        comment.delete()
        return redirect("post-detail", id=comment.post.id, slug=comment.post.slug)
    else:
        return redirect(
            "post-detail", id=comment.post.id, slug=comment.post.slug
        )
