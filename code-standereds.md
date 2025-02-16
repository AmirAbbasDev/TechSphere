# Django Tech Community Blog - Code Standards

To ensure consistency, readability, and maintainability across the codebase, all contributors must adhere to the following code standards. These guidelines will help us collaborate effectively and produce high-quality code.

---

## 1. **General Coding Standards**

- Follow **PEP 8** for Python code.
- Use **4 spaces** for indentation (no tabs).
- Keep lines to a maximum of **79 characters** (or 99 for slightly longer lines if necessary).
- Use descriptive variable and function names (e.g., `user_profile` instead of `up`).
- Avoid single-letter variable names unless in a very limited scope (e.g., loop counters).
- Write meaningful comments and docstrings to explain complex logic or functionality.
- Remove unused imports, variables, and commented-out code before committing.

---

## 2. **Project Structure**

Follow the standard Django project structure:

```
tech_blog/
├── manage.py
├── tech_blog/
│   ├── __init__.py
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── apps/
│   ├── blog/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   │   ├── blog/
│   │   │   │   ├── base.html
│   │   │   │   ├── post_list.html
│   │   │   │   ├── post_detail.html
│   │   ├── static/
│   │   │   ├── blog/
│   │   │   │   ├── css/
│   │   │   │   ├── js/
│   │   │   │   ├── images/
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── test_models.py
│   │   │   ├── test_views.py
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   ├── production.txt
├── .gitignore
├── README.md
├── LICENSE
```

---

## 3. **Django-Specific Standards**

### 3.1 **Models**

- Use singular names for models (e.g., `Post`, not `Posts`).
- Define `__str__` methods for models to ensure readability in the admin panel.
- Use `verbose_name` and `verbose_name_plural` for better readability.
- Add docstrings to describe the purpose of the model and its fields.
- Use Django's built-in validators and constraints where applicable.

Example:

```python
from django.db import models

class Post(models.Model):
    """Represents a blog post."""
    title = models.CharField(max_length=200, verbose_name="Post Title")
    content = models.TextField(verbose_name="Content")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
```

---

### 3.2 **Views**

- Use class-based views (CBVs) where possible for reusability and clarity.
- Use function-based views (FBVs) for simpler logic.
- Keep views concise and delegate business logic to models or utility functions.
- Use Django's built-in decorators like `@login_required` or `@permission_required` where applicable.

Example:

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    """Displays a list of all blog posts."""
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
```

---

### 3.3 **Templates**

- Use Django's template language for logic in templates.
- Avoid complex logic in templates; move it to views or models.
- Use template inheritance to avoid redundancy (e.g., `base.html`).
- Use meaningful block names in templates.

Example:

```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>{% block title %}Tech Blog{% endblock %}</title>
  </head>
  <body>
    <header>
      <h1>Tech Community Blog</h1>
    </header>
    <main>{% block content %}{% endblock %}</main>
  </body>
</html>

<!-- post_list.html -->
{% extends "blog/base.html" %} {% block title %}Post List - Tech Blog{% endblock
%} {% block content %}
<h2>Blog Posts</h2>
<ul>
  {% for post in posts %}
  <li>{{ post.title }} by {{ post.author }}</li>
  {% endfor %}
</ul>
{% endblock %}
```

---

### 3.4 **Static Files**

- Organize static files by app (e.g., `blog/static/blog/css/style.css`).
- Use meaningful file names for static assets.
- Use `{% static %}` template tag to reference static files.

Example:

```html
<link rel="stylesheet" href="{% static 'blog/css/style.css' %}" />
```

---

### 3.5 **URLs**

- Use `path()` instead of `url()` for defining URLs.
- Use namespaces for app-specific URLs.
- Use descriptive URL patterns.

Example:

```python
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
]
```

---

## 4. **Testing**

- Write unit tests for models, views, and forms.
- Use Django's `TestCase` for testing.
- Keep tests isolated and independent.
- Use descriptive test method names.

Example:

```python
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_post_creation(self):
        """Test if a post is created successfully."""
        post = Post.objects.create(title="Test Post", content="This is a test post.")
        self.assertEqual(post.title, "Test Post")
```

---

## 5. **Version Control**

- Use meaningful commit messages (e.g., "Add user authentication" instead of "Update code").
- Create feature branches for new features or fixes (e.g., `feature/user-auth`).
- Rebase your branch before creating a pull request.
- Review each other's code before merging.

---

## 6. **Documentation**

- Update the `README.md` file with project setup instructions.
- Add docstrings to all functions, classes, and methods.
- Document API endpoints if applicable.

---

## 7. **Environment Setup**

- Use `python-decouple` or `django-environ` for managing environment variables.
- Keep `settings.py` modular (e.g., `base.py`, `development.py`, `production.py`).
- Use `requirements.txt` or `Pipenv` for dependency management.

---

## 8. **Code Reviews**

- Always review each other's code before merging.
- Provide constructive feedback.
- Ensure all tests pass before merging.
