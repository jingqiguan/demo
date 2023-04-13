from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path(
        "trade/", views.trade, name="index"
    ),
    re_path(
        "trade/(?P<node>[\w\d_]+)/(?P<start>\d{4}-\d{2}-\d{2})/(?P<end>\d{4}-\d{2}-\d{2})/", views.trade, name="index"
    ),
    path("balance/", views.balance, name="index"),
    path("predict/", views.predict, name="index"),
    path("daily/", views.daily, name="index"),
]
