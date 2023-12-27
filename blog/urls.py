from django.urls import path
from blog.views import PostListView, CreatePostView, PostDetailView

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create', CreatePostView.as_view(), name='create_post'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='post_detail')
]
