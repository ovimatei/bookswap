import self as self
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .book import Book


class UserBook(models.Model):
    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'
    STATUS = [
        (AVAILABLE, _('Available to request')),
        (UNAVAILABLE, _('Offered to someone')),
    ]

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default=AVAILABLE,
    )

    def __str__(self):
        return "{} owned by {}".format(self.book_id, self.user_id)
