from rest_framework.routers import DefaultRouter
from tasks.views import *

router = DefaultRouter()
router.register('', TaskAPI, 'api_tasks')

urlpatterns = router.urls