from datetime import date

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.


class StartingPageView(ListView):
    model = Post
    paginate_by = 3
    template_name = "blog/index.html"
    ordering = ["-date"]
    context_object_name = "posts"

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     data = queryset[:3]
    #     return data


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(DetailView):
    model = Post
    template_name = "blog/post-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context
    
