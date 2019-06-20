from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils import timezone
from .models import Post
from .forms import PostCreateForm


# Create your views here.
class PostListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'posts/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostCreateView(SuccessMessageMixin, CreateView):
    form_class = PostCreateForm
    template_name = 'posts/create.html'
    success_message = "Created post successfully :)"


class PostUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'posts/update.html'
    model = Post
    fields = ['name', 'content']
    success_message = "Updated post successfully :)"

    def get_success_url(self):
        return reverse('posts:list', kwargs={})
