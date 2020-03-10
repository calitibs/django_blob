from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

from .models import BlongModel
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse


# Create your views here.

def blog_index(request):
    return render(request, 'demo_index.html')


def blog_add(request):
    if request.method == 'GET':
        return render(request, 'demo_add.html')

    elif request.method == 'POST':
        title = request.POST.get('title')  # 'title取name的值
        content = request.POST.get('content')

        print(title, content)
        # 保存数据到数据库
        blog = BlongModel(title=title, content=content)
        # blog = BlongModel(btitle=title,bpub_date=date(1988.1.1))
        blog.save()

        return render(request, 'demo_add.html')


def blog_list(request):
    blog_list = BlongModel.objects.all()
    # print(pages)
    p = Paginator(blog_list, 5)  # 分页 一页有5条数据
    page = request.GET.get('page') # 当前页面
    try:
        pages = p.page(page)
    except PageNotAnInteger:  # alt+enter快速导包
        pages = p.page(1) # 如果传的值不合法，默认第一页
    except EmptyPage:  # alt+enter快速导包
        pages = p.page(p.num_pages)
    return render(request, 'demo_list.html', context={'pages': pages, 'blog_list': blog_list})


def blog_detail(request, blog_id):
    blog = BlongModel.objects.get(id=blog_id)
    # print(blog)
    return render(request, 'demo_detail.html', context={'blog': blog})


def blog_delete(request, blog_id):
    blog = BlongModel.objects.get(id=blog_id)
    # print(blog)
    if blog:
        blog.delete()
        print(blog)
        return redirect(reverse('blog_list'))
    else:
        return HttpResponse('文章不存在')


def blog_update(request, blog_id):
    blog = BlongModel.objects.get(id=blog_id)
    # print(blog)
    if request.method == 'POST':
        blog.title = request.POST.get('title')  # 'title取demo_add中name的值
        blog.content = request.POST.get('content')  # 'title取name的值
        blog.save()
        return redirect(reverse('blog_list'))
    elif request.method == 'GET':
        return render(request, 'update.html', context={'blog': blog})
