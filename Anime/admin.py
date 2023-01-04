from django.contrib import admin
from Anime.models import UploadAnime, UploadVideo, UploadMovie, Comment

# Register your models here.


class UploadVideoInline(admin.TabularInline):
    model = UploadVideo

class CommentInline(admin.TabularInline):
    model = Comment

class UploadAnimeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name','author','description','cover','ongoing','date_of_release']}),
        ('Genres', {'fields': ['action','adventure','comedy','drama','ecchi','fantasy','harem',
                                'horror','isekai','magic','martial_arts','mecha',
                                'military','music','mystery','psychological','romance','school',
                                'sci_fi','slice_of_life','shounen','sports','supernatural','tragedy'],
                    'classes': ['collapse', 'open'],
                    }),
    ]
    inlines = [
        UploadVideoInline,
        CommentInline,
    ]

class UploadMovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name','author','description','cover','ongoing','date_of_release']}),
        ('Genres', {'fields': ['action','adventure','comedy','drama','ecchi','fantasy','harem',
                                'horror','isekai','magic','martial_arts','mecha',
                                'military','music','mystery','psychological','romance','school',
                                'sci_fi','slice_of_life','shounen','sports','supernatural','tragedy'],
                    'classes': ['collapse', 'open'],
                    }),
    ]
    inlines = [
        UploadVideoInline,
        CommentInline,
    ]

class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Comment', {
            'fields': ['author', 'text', 'created_date', 'approved_date'],
            'classes': ['collapse', 'open']
            }),
    ]
admin.site.register(UploadAnime, UploadAnimeAdmin)
admin.site.register(UploadMovie, UploadMovieAdmin)
admin.site.register(UploadVideo)
admin.site.register(Comment, CommentAdmin)
