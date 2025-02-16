from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from apps.blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "status"]
        content = CKEditor5Widget(
            attrs={"class": "django_ckeditor_5"}, config_name="extends"
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
