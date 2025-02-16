from django.contrib import admin
from .models import Post, Comment

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "publish", "status"]
    list_filter = ["status", "created_at", "publish", "author"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "user", "post", "created_at", "updated_at"]
