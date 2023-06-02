from django.contrib import admin

from blog.models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
    )


class LocationAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'name',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
    )
    list_editable = (
        'category',
    )
    search_fields = ('title', 'pub_date', 'category',)
    list_filter = ('is_published', 'pub_date', 'category',)
    list_display_links = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
