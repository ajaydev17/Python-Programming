"""
In Django, a ManyToManyField defines a many-to-many relationship between
models, meaning that each record in one model can relate to multiple records in another
model, and vice versa. Unlike a ForeignKey, which establishes a one-to-many relationship, a
ManyToManyField creates a separate intermediary table that links the records of the two
models, allowing bidirectional associations.

For instance, in a blog application, ManyToManyField might be used to link Post and Tag
models since each post can have multiple tags, and each tag can be associated with multiple
posts.
"""

# in models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='posts')


class Tag(models.Model):
    name = models.CharField(max_length=50)


# usage
post = Post.objects.create(title='First Post', content='Content of the first post')
tag = Tag.objects.create(name='Python')
post.tags.add(tag)