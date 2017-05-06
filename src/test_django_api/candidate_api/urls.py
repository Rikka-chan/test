from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from candidate_api import views

urlpatterns = [
    url(r'^candidates/$', views.CandidateList.as_view()),
    url(r'^candidates/(?P<pk>[0-9]+)/$', views.CandidateDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)