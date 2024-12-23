from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
    articles=Article.objects.all().order_by('date')
    return render (request,'articles/articles_list.html', {'articles':articles} )


def article_detail(request, slug):
    articles=Article.objects.get(slug=slug)
    return render (request,'articles/articles_detail.html', {'articles':articles} )


@login_required(login_url="/login/")
def create_view(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instanse=form.save(commit=False)
            instanse.author=request.user
            instanse.save()
            return redirect('articles:list')
    else:
        form=forms.CreateArticle()
    return render(request,'articles/create.html', {'form':form})