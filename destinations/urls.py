from rest_framework.routers import DefaultRouter
from .views import DestinationViewSet, DestinationCategoryViewSet

router = DefaultRouter()
router.register(
    "destinations",
    DestinationViewSet,
    basename="destination",
)
router.register(
    "categories",
    DestinationCategoryViewSet,
    basename="category",
)

urlpatterns = router.urls