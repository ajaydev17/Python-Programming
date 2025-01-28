"""
Django’s ContentType framework allows for generic relationships, which enable
models to relate to other models without explicitly defining a foreign key. This is useful for
scenarios where a model needs to interact with different types of models dynamically.
The ContentType framework uses a ContentType model to store information about all
models in an app, allowing developers to create fields that reference other models
generically.
"""

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

class Comment(models.Model):
    content = models.TextField()
    # GenericForeignKey fields require two attributes: content_type and object_id
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # GenericForeignKey field to link to any model
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.content


# Example usage
content_type = ContentType.objects.get_for_model(Post)
comment = Comment.objects.create(content='Nice post!', content_type=content_type, object_id=1)