from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from book.views import *

urlpatterns = [
                  path('', BookListView.as_view(), name="home"),
                  path('about/', about, name="about"),
                  path('profile/', user_profile, name="user_profile"),
                  path('book/<slug>/', BookDetailView.as_view(), name="book"),
                  path('add/', BookAddView.as_view(), name="add_book"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
