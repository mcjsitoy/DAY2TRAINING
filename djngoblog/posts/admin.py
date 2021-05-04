from django.contrib import admin

from .models import Articles, ArticleComment, ArticleLikes


# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    model = Articles
    fieldsets = (
       
        (None, {'fields': ('title', 'description','content','owner',)}),
        
    )

    add_fieldsets=(
        (None,{
            'classes': ('wide',),
            
            'fields': ('title','description','content','owner',)}
        ),
    )


class ArticleCommentAdmin(admin.ModelAdmin):
    model=ArticleComment
    fieldsets=(
        (None,{'fields':('user','comment','article','date_created,date_updated',)}),
    )

    add_fieldsets=(
        (None,{
            'classes': ('wide',),
            'fields':('user','comment','article','date_created,date_updated',)
        })
    )

class ArticleLikesAdmin(admin.ModelAdmin):
    model=ArticleLikes
    fieldsets=(
        (None,{
            'fields':('user','article','is_liked',)
        }),
    )

    add_fieldsets=(
        (None,{
        'classes': ('wide',),
        'fields':('user','article','is_liked',)
    })
    )

admin.site.register(Articles, ArticlesAdmin),
admin.site.register(ArticleComment, ArticleCommentAdmin),
admin.site.register(ArticleLikes, ArticleLikesAdmin)