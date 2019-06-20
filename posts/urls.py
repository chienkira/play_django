from django.urls import path
from posts.views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
)

app_name = 'posts'

urlpatterns = [
    path('list/', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
]
