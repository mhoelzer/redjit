from django.db import models
from redjit.redjiter.models import Redjiter
from redjit.subredjit.models import Subredjit



class Post(models.Model):
    user = models.ForeignKey(Redjiter, on_delete=models.CASCADE, null=True)
    subredjit = models.ForeignKey(Subredjit, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=200)
    upvotes = models.ManyToManyField(Redjiter, related_name='upvotes', blank=True)
    downvotes = models.ManyToManyField(Redjiter, related_name='downvotes', blank=True)

    def get_score(self):
        return self.upvotes.count() = self.downvotes.count()
