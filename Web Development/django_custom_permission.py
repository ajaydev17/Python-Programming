"""
Django provides a default permission system, but custom permissions can be added
by defining permissions in models and checking them in views. Custom permissions are
typically managed using Django’s has_perm method or by creating custom decorators to
enforce permissions at the view level.
"""

# # in models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_published = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ('can_publish_article', 'Can publish articles'),
            ('can_edit_article', 'Can edit articles'),
        ]


# in views.py
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

@permission_required('myapp.can_publish_article')
def publish_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.is_published = True
    article.save()
    return HttpResponse('Article published successfully!')