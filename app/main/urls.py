from django.urls import path
from .views import IndexView, DocumentDetailView, SearchResultsView

app_name = "main"
urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    # path("view/", DocumentDetailView.as_view(), name="document"),
    path("view/<str:id>/", DocumentDetailView.as_view(), name="document"),
    path('search/<str:q>/', SearchResultsView.as_view(), name='search_results'),
]
