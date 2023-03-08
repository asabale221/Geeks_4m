from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from django.views import generic
from django.urls import reverse_lazy


def hello(request):
    body = "<h1>Hello</h1>"

    headers = {"name":"Alex",
                "Content-type":"application/vnd.ms-excel",
                "Content-Disposition":"attachment; filename = file.xls"
                }
    return HttpResponse(body, headers = headers, status = 500)

class IndexView(generic.ListView):
    queryset = Post.objects.filter(status=True)
    context_object_name = "posts"
    # model = Post
    template_name = "posts/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"


class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")


class AboutView(generic.TemplateView):
    template_name = "posts/about.html"
    extra_context = {
        "title": "Страница о нас",
    }


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-page")

def get_index(request):
    posts  = Post.objects.filter(status=True)
    # print(request.user)
    # if request.method == "GET":
    #     return HttpResponse("Главная страница")
    # else:
    #     return HttpResponse("Не тот запрос")

    context = {
        "title": "Main page",
        "posts": posts,
    }
    return render(request, "posts/index.html", context=context)


def get_contacts(request):
    context = {
        "title": "Контакт"
    }
    return render(request, "posts/contacts.html", context=context)

    # return HttpResponse("Контакты")


def get_about(request):
    context = {
        "title": "O нас"
    }
    return render(request, "posts/about.html", context=context)


def get_post(request):
    context = {
        "title": "Пост",
    }
    return render(request, "posts/post_create.html", context=context)


def update_post(request):
    context = {
        "title": "Пост",
    }
    return render(request, "posts/post_update.html", context=context)


def delete_post(request):
    context = {
        "title": "Пост",
    }
    return render(request, "posts/post_detail.html", context=context)
# Create your views here.