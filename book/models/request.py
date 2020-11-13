from django.db import models

from .user_book import UserBook


class Request(models.Model):
    status = models.CharField(max_length=64)
    requested_book = models.ForeignKey(UserBook, related_name="requested_for_change", on_delete=models.CASCADE)
    offered_book = models.ForeignKey(UserBook, related_name="offered_for_change",  on_delete=models.CASCADE)
    request_date = models.DateField(auto_now=True)

    def __str__(self):
        return "{} change for {}".format(self.requested_book, self.offered_book)
