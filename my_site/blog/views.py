from datetime import date

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Post
from .forms import CommentForm

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


class SinglePostView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts", [])
        is_saved_for_later = post_id in stored_posts
        return is_saved_for_later

    def __render_context(self, request, post):

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-details.html", context)

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        return self.__render_context(request, post)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-details-page", args=[slug]))

        return self.__render_context(request, post)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts", [])
        context = {}

        if len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts", [])
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
            return HttpResponseRedirect("/")
        else:
            stored_posts.remove(post_id)
            request.session["stored_posts"] = stored_posts
            
            current_post = Post.objects.get(id=post_id)
            current_post_slug = current_post.slug

            return HttpResponseRedirect(reverse("post-details-page", args=[current_post_slug]))
