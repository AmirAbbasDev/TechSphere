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


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentUpdateForm(forms.Form):
    content = forms.CharField(required=False, widget=forms.Textarea)
