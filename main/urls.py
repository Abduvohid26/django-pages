from .views import HomepageWiev,AboutpageWiev
from django.urls import path


urlpatterns = [
    path('',HomepageWiev.as_view(),name='home'),
    path('about/',AboutpageWiev.as_view(),name='about'),
]