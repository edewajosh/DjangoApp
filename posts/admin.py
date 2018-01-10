from django.contrib import admin

# Register your models here.
from .models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

admin.site.register(Posts, PostsAdmin)
