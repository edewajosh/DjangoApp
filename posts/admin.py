from django.contrib import admin

# Register your models here.
from .models import Posts, Comments

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title',"author", 'created_at')

admin.site.register(Posts, PostsAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('text','post', 'pub_date')

admin.site.register(Comments, CommentsAdmin)