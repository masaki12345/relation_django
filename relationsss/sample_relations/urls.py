from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import multiViewSet, multi2ViewSet, multi3ViewSet, multi4ViewSet, jobViewSet
# from .views import multiListCreateApiView

router = routers.DefaultRouter()
router.register('multi', multiViewSet)
router.register('job', jobViewSet)
# router.register('ps', multi3ViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path("job/", JobListCreateApiView.as_view(), name="job_list"),

    # path('multi/s/', multi2ViewSet.as_view()),
    # path('multi/s/', multiViewSet.as_view({'post': 'list'})),
    # path('multi/sｓ/', multiViewSet.as_view({'get': 'list'})),
    # path('multi/sss/', multiViewSet.as_view({'put': 'list'})),
    # path('multi/ssss/', multiViewSet.as_view({'patch': 'list'})),
    # path('multi/s/', multi3ViewSet.as_view()),
    # path('multi/s/', multi4ViewSet.as_view()),

]
