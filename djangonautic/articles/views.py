from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def index(request):
    articles=Article.objects.all().order_by('date')
    return render(request,'articles/index.html',{'articles':articles})
def article_dis(request,slug):
    # return HttpResponse(slug)
    article=Article.objects.get(slug=slug)
    return render(request,'articles/art_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def create(request):
    if request.method=='POST':
        form=forms.Create(request.POST,request.FILES)
        if form.is_valid():
            #save article to db
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('articles:index')
    else:
        form=forms.Create()
    return render(request,'articles/create.html',{'form':form})