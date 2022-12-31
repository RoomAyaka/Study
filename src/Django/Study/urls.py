from django.urls import path
from . import views

app = 'Study'
urlpatterns = [
    path("page/<int:page_id>/", views.page, name='page'),
    path("index/", views.index, name='index'),
]
