from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from blog.models import Post
from blog.forms import PostForm


class PostListView(ListView):
    template_name = 'blog/post_list.html'
    model = Post
    paginate_by = 10


class CreatePostView(CreateView):
    template_name = 'blog/create_post.html'
    form_class = PostForm


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
