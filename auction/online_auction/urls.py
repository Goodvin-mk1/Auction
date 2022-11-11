from django.urls import path, include
from .views import IndexView, SearchView, AboutView, LotCreateView, LotUpdateView, LotDetailView, LotDeleteView, \
    ProfileView, AuctionSearchView, AuctionCreateView, AuctionDetailView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', IndexView.as_view()),
    path('search/', SearchView.as_view()),
    path('about/', AboutView.as_view()),
    path('lot/add/', LotCreateView.as_view()),
    path('lot/<int:pk>/detail/', LotDetailView.as_view()),
    path('lot/<int:pk>/update/', LotUpdateView.as_view()),
    path('lot/<int:pk>/delete/', LotDeleteView.as_view()),
    path('accounts/profile/', ProfileView.as_view()),
    path('auction/add/', AuctionCreateView.as_view()),
    path('auction/<int:pk>/detail/', AuctionDetailView.as_view()),
    path('auction-search/', AuctionSearchView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
