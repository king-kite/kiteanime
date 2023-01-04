from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from Anime.models import UploadAnime, UploadVideo, UploadMovie, Comment
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.utils.timezone import now
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseRedirect
from Anime.forms import CommentForm

# Create your views here.

class Homes(ListView):
    model = UploadVideo
    template_name = 'homes.html'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        kwargs = super(Homes, self).get_context_data(**kwargs)

        latest_series = UploadAnime.objects.all().order_by('-date_of_release')[:6]
        latest_movies = UploadMovie.objects.all().order_by('-date')[:6]

        latest_updates = UploadVideo.objects.all().order_by('-vdate')[:100]
        paginator = Paginator(latest_updates, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            latest_updates = paginator.page(page)
        except PageNotAnInteger:
            latest_updates = paginator.page(1)
        except EmptyPage:
            latest_updates = paginator.page(paginator.num_pages)

        kwargs.update({
            'UploadAnime': UploadAnime.objects.all(),
            'latest_series': latest_series,
            'latest_movies': latest_movies,
            'latest_updates': latest_updates,
        })
        return kwargs


class LatestSeries(ListView):
    model = UploadAnime
    template_name = 'latest_series.html'

    def get_context_data(self, **kwargs):
        latest_series = UploadAnime.objects.all().order_by('name')
        kwargs = super(LatestSeries, self).get_context_data(**kwargs)
        kwargs.update({
            'latest_series': latest_series,
        })
        return kwargs

class TopRated(ListView):
    model = UploadAnime
    template_name = 'top_rated.html'

    def get_context_data(self, **kwargs):
        top_rated = UploadAnime.objects.all().order_by('-rated', '-date')[:6]
        kwargs = super(TopRated, self).get_context_data(**kwargs)
        kwargs.update({
            'top_rated': top_rated,
        })
        return kwargs

class LatestMovie(ListView):
    model = UploadMovie
    template_name = 'latest_movies.html'

    def get_context_data(self, **kwargs):
        latest_movies = UploadMovie.objects.all().order_by('-date')[:6]
        kwargs = super(LatestMovie, self).get_context_data(**kwargs)
        kwargs.update({
            'latest_movie': latest_movies,
        })
        return kwargs

class Home(ListView):
    model = UploadVideo
    template_name = 'home.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs = super(Home, self).get_context_data(**kwargs)
        latest_updates = UploadVideo.objects.all().order_by('-vdate')[:60]
        paginator = Paginator(latest_updates, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            latest_updates = paginator.page(page)
        except PageNotAnInteger:
            latest_updates = paginator.page(1)
        except EmptyPage:
            latest_updates = paginator.page(paginator.num_pages)

        kwargs.update({
            'UploadAnime': UploadAnime.objects.all(),
            'latest_updates': latest_updates,
        })
        return kwargs
    

class SearchView(ListView):
    model = UploadAnime
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        object_list = UploadAnime.objects.filter(Q(name__icontains=query))
        list = UploadAnime.objects.all()
        return render(request, 'search.html', {'list': list, 'object_list': object_list, 'query':query})


def View(request, pk):
    try:
        object = UploadAnime.objects.get(pk=pk)
        object_list = object.videos.all()
        view_name = UploadAnime.objects.get(pk=pk)
        ongoing_list = UploadAnime.objects.all()
        paginator = Paginator(object_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except UploadAnime.DoesNotExist:
        raise Http404("Sorry, this Anime does not exist.")
    return render(request, 'view.html', {'object_list': object_list,'page_obj': page_obj, 'view_name': view_name, 'ongoing_list':ongoing_list})

"""
Try using DetailView instead of ListView
class View(ListView):
    model = UploadAnime
    template_name = 'animeview.html'

    def get_context_data(self, pk, **kwargs):
        object = UploadAnime.objects.get(pk=pk)
        object_list = object.videos.all()
        view_name = UploadAnime.objects.get(pk=pk)
        ongoing_list = UploadAnime.objects.all()
        paginator = Paginator(object_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        kwargs = super(View, self).get_context_data(**kwargs)
        kwargs.update({
            'object_list': object_list,
            'page_obj': page_obj,
            'ongoing_list': ongoing_list,
            'view_name': view_name,
        })
"""

class AnimeList(ListView):
    model = UploadAnime
    template_name = 'anime_list.html'


class Watch_and_Download(ListView):
    model = UploadVideo
    template_name = 'watch_and_download.html'
    

    def get_context_data(self, pk, **kwargs):
        video_list = UploadVideo.objects.get(pk=pk)
        ongoing_list = UploadAnime.objects.all()
        qs = video_list.foreign.videos.order_by('title', 'pk')
        next = qs.filter(pk__gt=video_list.pk).order_by('pk').first()
        previous = qs.filter(pk__lt=video_list.pk).order_by('-pk').first()
        kwargs = super(Watch_and_Download, self).get_context_data(**kwargs)
        kwargs.update({
            'video_list': video_list,
            'ongoing_list': ongoing_list,
            'qs': qs,
            'next': next,
            'previous': previous,
        })
        return kwargs

"""
def Watch_and_Download(request, pk):
    video_list = UploadVideo.objects.get(pk=pk)
    ongoing_list = UploadAnime.objects.all()
    qs = video_list.foreign.videos.order_by('title', 'pk')
    next = qs.filter(pk__gt=video_list.pk).order_by('pk').first()
    previous = qs.filter(pk__lt=video_list.pk).order_by('-pk').first()
    
    return render(request, 'watch_and_download.html', {
        'video_list': video_list,
        'ongoing_list': ongoing_list,
        'next': next,
        'previous': previous
    })
"""

def Comments(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    approved_comment = Comment.objects.filter(approved_comment=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commite=False)
            new_comment.post = comment
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'latest_series.html', {'comment_form': comment_form,
                                                    'approved_comment': approved_comment,
                                                    'new_comment': new_comment})