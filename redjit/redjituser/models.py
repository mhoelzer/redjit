from django.db import models

from django.contrib.auth.models import User


class RedjitUser(models.Model):
    """Handling permissions for community moderator AKA ability to delete other peoples comments?
    https://www.vinta.com.br/blog/2016/controlling-access-a-django-permission-apps-comparison/
    https://www.programcreek.com/python/example/50077/django.contrib.auth.models.Permission"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=30)
    # email = models.EmailField(
    #     max_length=70, null=True, blank=True, unique=True)
    following = models.ManyToManyField(
        'self', related_name='followed_by', symmetrical=False, blank=True, null=True)

    def __str__(self):
        return self.user

    # permission = models.Permission()

    # class Meta:
    #     permissions = (
    #         ('community_moderator', 'Community Moderator'),
    #     )
