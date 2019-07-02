from django.shortcuts import render, reverse, 
from django.http import HttpResponseRedirect
from .forms import PostForm
from .models import Post
from .helper import toggle_comment_upvotes, sort_comments
from django.views import View
from redjit.comment.forms import CommentForm
from redjit.comment.models import Comment



class MyPost(View):
    form_class = PostForm

    def get(self, request):
        form = self.form_class()
        return render(request, './post/newpost.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('register'))
        form = self.form_class()
        return render(request, './post/newpost.html', {'form': form})

class PostView(View):
    form_class = CommentForm

    def get(self, request, subredjit, post_id):
        response = {}
        post = Post.objects.get(id=post_id)
        comments = sort_comments(post.comment_set.get_queryset())
        response.update({'post': post})
        response.update({'form': self.form_class()})
        response.update({'comments': comments})
        return render(request, './post/post.html', response)

    def post(self, request, subredjit, post_id):
        form = self.form_class(request.POST)
        toggle_comment_upvotes(request)
        if form.is_valid():
            data = form.cleaned_data
            Comments.objects.create(
                body=data['body'],
                user=request.user.redjiter,
                post=Post.objects.get(id=post_id)
            )
        return HttpResponseRedirect(reverse('post', kwargs={'subredjit': subredjit,
                                    'post_id': post_id}))