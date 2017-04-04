from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    status_id = models.IntegerField(primary_key=True, null=False)
    status_message = models.TextField(max_length=None)
    link_name = models.TextField(max_length=None)
    status_type = models.TextField(max_length=None)
    status_published = models.TextField(max_length=None)
    num_reactions = models.TextField(max_length=None)
    num_comments = models.TextField(max_length=None)
    num_shares = models.TextField(max_length=None)
    num_likes = models.TextField(max_length=None)
    num_loves = models.TextField(max_length=None)
    num_wows = models.TextField(max_length=None)
    num_hahas = models.TextField(max_length=None)
    num_sads = models.TextField(max_length=None)
    num_angry = models.TextField(max_length=None)
    label = models.TextField(max_length=None)

class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True, null=False)
    status_id = models.IntegerField(null=False)
    parent_id = models.TextField(max_length=None)
    comment_message = models.TextField(max_length=None)
    comment_author = models.TextField(max_length=None)
    comment_published = models.TextField(max_length=None)
    comment_likes = models.TextField(max_length=None)
    label = models.TextField(max_length=None)
    nework = models.TextField(max_length=None)
    category = models.TextField(max_length=None)