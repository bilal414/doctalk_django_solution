from rest_framework import routers
from .views import ProfileView

router = routers.SimpleRouter()

router.register(r"profiles", ProfileView, basename="")
urlpatterns = router.urls

