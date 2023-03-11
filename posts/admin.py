from django.contrib import admin
from posts.models import Post, Comment


# Простой способ регистрации моделей в админке
# admin.site.register(Post)




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "status"]
    list_filter = ["status", ]
    list_editable = ["status", ]
    
# Развернутый способ

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "name", "created"]