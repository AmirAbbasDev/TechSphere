import re

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.mail import EmailMessage

from blog.forms import CommentForm, PostForm, CommentUpdateForm, EmailPostForm

from .models import Comment, Post


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 3
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


def article_detail_view(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    form = CommentForm()
    comment_update_form = CommentUpdateForm()
    comments = Comment.objects.filter(post=post)
    # add_comment_to_post(request, post)
    context = {
        "form": form,
        "commentupdateform": comment_update_form,
        "comments": comments,
        "post": post,
    }
    return render(request, "blog/post_detail.html", context)


@login_required
def add_comment_to_post_view(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(post.get_absolute_url())


@login_required
def delete_comment_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    url_parms = [
        comment.post.publish.year,
        comment.post.publish.month,
        comment.post.publish.day,
        comment.post.slug,
    ]

    if request.user == comment.user or request.user.is_staff:
        comment.delete()
        return redirect(reverse("post-detail", args=url_parms))
    else:
        return redirect(reverse("post-detail", args=url_parms))


@login_required
def comment_update_view(request, comment_id):
    if request.method == "POST":
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentUpdateForm(request.POST)
        url_parms = [
            comment.post.publish.year,
            comment.post.publish.month,
            comment.post.publish.day,
            comment.post.slug,
        ]
        if form.is_valid():
            comment.content = form.cleaned_data["content"]
            comment.save()
            return redirect(reverse("post-detail", args=url_parms))


def post_share_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = _(
                f"{clean_data['name']} ({clean_data['email']})"
                f"recommends you read {post.title}"
            )
            email_body = _(
                f"Read {post.title} at {post_url}\n\n"
                f"{clean_data['name']}'s comments: {clean_data['comments']}"
            )
            email_message = EmailMessage(
                subject,
                email_body,
                settings.EMAIL_HOST_USER,
                [clean_data["to"]],
            )
            email_message.send(fail_silently=True)
            return redirect(post.get_absolute_url())
    else:
        form = EmailPostForm()
    context = {"post": post, "form": form, "sent": sent}
    return render(request, "blog/post/share.html", context)
