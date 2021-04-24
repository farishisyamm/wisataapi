from wisataapi.viewsets import WisataViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register("wisata", WisataViewset)