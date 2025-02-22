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



def article_detail_view(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    comments = Comment.objects.filter(post=post).order_by("-created_at")
    form = CommentForm()

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("post_detail", id=id, slug=slug)

    return render(request, "blog/post_detail.html", {"post": post, "comments": comments, "form": form})

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
            # return redirect("post-detail", slug=post.slug)
            return redirect("post_detail", id=post.id, slug=post.slug)




@login_required
def delete_comment_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure the logged-in user owns the comment
    if request.user == comment.user:
        post = comment.post  # Assign post before using it
        comment.delete()
        return redirect("post_detail", id=post.id, slug=post.slug)
    
    return redirect("post_detail", id=comment.post.id, slug=comment.post.slug)



@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure the logged-in user owns the comment
    if request.user != comment.user:
        return redirect("post_detail", id=comment.post.id, slug=comment.post.slug)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", id=comment.post.id, slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, "blog/partials/update_comment.html", {"form": form, "comment": comment})