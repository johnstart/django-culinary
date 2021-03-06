from django.conf.urls.defaults import *
from culinary.models import *
from culinary.views import PostView, Main, ArchiveMonth

urlpatterns = patterns("dbe.culinary.views",
   (r"^post/(?P<dpk>\d+)/$", PostView.as_view(), {}, "post"),
   (r"^archive_month/(\d+)/(\d+)/$", ArchiveMonth.as_view(), {},
    "archive_month"),
   (r"^$", Main.as_view(), {}, "main"),
)
