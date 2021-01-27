from django.shortcuts import render,get_object_or_404,redirect
from .models import post,comment
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import Emailpostform
from django.core.mail import send_mail
# Create your views here.

def post_list(request):
    total=len(comment.objects.all())
    banner=post.published.all()[:3]
    articles=post.published.all()[3:]
    paginator=Paginator(articles,2)
    page=request.GET.get('page')
    print(page)
    try:
        posts=paginator.page(page)
        print("ashish",post)
    except PageNotAnInteger:
        posts=paginator.page(1)
       
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    print(articles)
    print(posts)
    print(page)
    return render(request,'base.html',{'articles':posts,'page':page,'banner':banner,'total':total})

def post_details(request,id):
    print("yes")
    article=get_object_or_404(post,id=id,status='published')
    comments=comment.objects.all()
    total=len(comments)
    #return render(request,html,{'article':article})
    print(article)
    return render(request,'details.html',{'article':article,'total':total,'comments':comments})
def about(request):
    return render(request,'about.html')


def sharepost(request,id):
    article=get_object_or_404(post,id=id,status='published')
    print(article)
    sent=False
    if request.method=='POST':
        form=Emailpostform(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(article.get_absolute_url())
            subject	='{}({}) recommends	you	reading	" {}"'.format(cd['name'],cd['email'],article.title)
            message	="read this post it is amazing at {}".format(post_url)
            send_mail(subject,	message,'admin@myblog.com',[cd['to']])
            sent=True
    else:
        form=Emailpostform()
    return render(request,'share.html',{'post':article,'sent':sent,'form':form})

def add_comment(request,id):
    if request.method=='POST':
        article=get_object_or_404(post,id=id,status='published')
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        c=comment(post=article,name=name,email=email,body=message)
        c.save()
    return redirect('blog:post_details',id=id)