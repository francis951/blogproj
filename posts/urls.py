from django.urls import path
from .views import PostView, UserView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("users", UserView, basename="users")
router.register("", PostView, basename="posts")
urlpatterns = router.urls