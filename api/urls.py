from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoardView, TuskView

router = DefaultRouter()
router.register('boards', BoardView, basename='board')
router.register('tusks', TuskView, basename='tusk')

urlpatterns = router.urls
