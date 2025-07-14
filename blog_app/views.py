from django.shortcuts import render
from blog_app.models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html",{"posts": posts})
def post_detaili(request, id):
    post =Post.objects.all(id=id)
    return render(request, "post_detail.html",{"post":post}),
