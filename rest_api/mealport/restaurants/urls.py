from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, MenuItemViewSet

router = DefaultRouter()
router.register('restaurants', RestaurantViewSet)
router.register('menu-items', MenuItemViewSet)

urlpatterns = router.urls
