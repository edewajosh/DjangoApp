from django.contrib import admin

# Register your models here.
from .models import Posts, Comments

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title',"author", 'created_at')

admin.site.register(Posts, PostsAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('text','post', 'pub_date')
<<<<<<< HEAD
    #field = ('text')
=======
>>>>>>> 642777593c591710c4a698a21a6e22d82d0bccdb

admin.site.register(Comments, CommentsAdmin)