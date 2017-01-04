from django.conf.urls import url, include
from . import views

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'feeders', views.FeederViewSet)
router.register(r'd_overhead_lines', views.DOverheadLineViewSet)
router.register(r'd_ohl_configurations', views.DOverheadLineConfigViewSet)
router.register(r'd_linespacings', views.DLineSpacingViewSet)
router.register(r'd_ohl_conductors', views.DOverheadLineConductorViewSet)

router.register(r'd_buses', views.DBusViewSet)
router.register(r'd_loads', views.DLoadViewSet)
router.register(r'd_generators', views.DGeneratorViewSet)
router.register(r'd_capacitors', views.DCapacitorViewSet)
router.register(r'd_solars', views.DSolarViewSet)
router.register(r'd_storages', views.DStorageViewSet)
router.register(r'd_batterys', views.DBatteryViewSet)




#nested?
# overheadlines_router = routers.NestedSimpleRouter(router, r'overheadlines', lookup='overheadline')
# overheadlines_router.register(r'configurations', views.DOverheadLineConfigViewSet, base_name='overheadline-configuration')


urlpatterns = [
    url(r'^$', views.test, name='home'),
    url(r'^testui/$', views.testui),
    url(r'^feederData/$', views.feederDataTest),
    url(r'^api/', include(router.urls)),
    # url(r'^api/', include(overheadlines_router.urls)),

]