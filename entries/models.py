from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Entry(models.Model):

    entry_title = models.CharField(max_length=50)
    entry_text = RichTextField(blank=True, null=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return f'{self.entry_title}'
