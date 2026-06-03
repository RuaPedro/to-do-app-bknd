from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, SubTaskViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'subtasks', SubTaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls
