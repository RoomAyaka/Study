from django.urls import path
from . import views

app = 'Study'
urlpatterns = [
    # as_view(): dispatchメソッドを利用する事が出来ます。
    path('', views.IndexView.as_view(), name='index'),
    path('article/<int:pk>/', views.ArticleView.as_view(), name='article'),
    path('article/new/', views.Newview.as_view(), name='new'),
]
