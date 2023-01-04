from django.urls import path, include
from Anime.views import Home, View, SearchView, AnimeList, Watch_and_Download, LatestSeries, Homes


from django.conf import settings #Only to be used in development and not production.
from django.conf.urls.static import static # Only to be used in development and not production.




urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('home/', Homes.as_view(), name = 'homes'),
    path('view/<str:pk>/', View, name = 'view'),
    path('search/', SearchView.as_view(), name = 'search'),
    path('anime_list/', AnimeList.as_view(), name = 'anime_list'),
    path('download/<int:pk>/', Watch_and_Download.as_view(), name ='watch_and_download'),
    path('latest_series/', LatestSeries.as_view(), name = 'latest_series'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Note: This is used only in development and not to be used in production.