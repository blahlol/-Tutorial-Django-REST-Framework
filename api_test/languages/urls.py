from django.urls import path,include
from rest_framework import routers
from . import views



router=routers.DefaultRouter()
router.register('languages',views.LanguageView)
router.register('paradigm',views.ParadigmView)

urlpatterns = [
    path('all/',views.list,name="list"),
    path('',include(router.urls)),
]
