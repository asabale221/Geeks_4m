from django.contrib import admin
from posts.models import Post

# Простой способ регистраций моделей в админке
# admin.site.register(Post)

# Развернутый способ регистраций моделей в админке

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "status"]
    list_filter = ['status',]