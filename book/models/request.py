from django.db import models

from .user_book import UserBook


class Request(models.Model):
    status = models.CharField(max_length=64)
    requested_book = models.ForeignKey(UserBook, on_delete=models.CASCADE)
    offered_book = models.ForeignKey(UserBook, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now=True)
