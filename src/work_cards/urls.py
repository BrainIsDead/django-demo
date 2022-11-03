from rest_framework import routers

from work_cards.views import WorkCardViewSet

router = routers.DefaultRouter()


router.register(r'work_cards', WorkCardViewSet, basename='work_cads')

urlpatterns = router.urls
