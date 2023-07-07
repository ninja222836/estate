from django.urls import path

from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('search/', SearchView.as_view(), name='Search_result'),
    path('property/<slug:property_slug>', property, name='Property'),
]

htmx_urlpatterns = [
    path('search-property/', search_property, name='Search_property'),
]

urlpatterns += htmx_urlpatterns