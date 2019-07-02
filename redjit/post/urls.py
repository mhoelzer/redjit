from django.urls import path
from redjit.post.views import MyPost, PostView


urlpatterns = [
    path('newpost/', MyPost.as_view(), name='newpost'),
    path('subredjit/<subredjit>/<post_id>/', PostView.as_view(), name='post')
]
