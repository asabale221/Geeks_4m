from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post


def hello(request):
    # my_list = [1, 2, 3, 4]
    body = "<h1>Hello</h1>"
    # body = """
    # <!DOCTYPE html>
    #     <html>
    #         <head>
    #             <title>Geek TEST</title>
    #         </head>
    #         <body>
    #
    #             <h1>Заголовок первого уровня</h1>
    #             <p>Параграф</p>
    #
    #         </body>
    #     </html>
    # """
    headers = {"name": "Alex", }
    # "Content-Type": "application/vnd.ms-excel",
    # "Content-Disposition": "attachment; filename=file.xls"}
    return HttpResponse(body, headers=headers, status=500)

def get_index(request):
    posts = Post.objects.filter(status=True)
    context = { 
        "title": 'Main Page', 
        "posts": posts,
    }
    return render(request, 'posts/index.html', context=context)

def get_about(request):
    context = { 
        "title": 'Страница о нас',
    }
    return render(request, "posts/about.html", context=context)

def get_contacts(request):
    context = { 
        "title": 'Контакты',
    }
    return render(request, "posts/contact.html", context=context)

def get_post(request):
    context = { 
        "title": 'Контакты',
    }
    return render(request, "posts/post_detail.html", context=context)

def update_post(request):
    context = { 
        "title": 'Контакты',
    }
    return render(request, "posts/post_update.html", context=context)

def delete_post(request):
    context = { 
        "title": 'Контакты',
    }
    return render(request, "posts/post_create.html", context=context)