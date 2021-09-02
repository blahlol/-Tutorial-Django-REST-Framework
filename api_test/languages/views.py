from django.shortcuts import render
from .models import Language,Paradigm
from .serializers import LanguageSerializer,ParadigmSerializer
from rest_framework import viewsets,permissions
from django.core.paginator import Paginator

class LanguageView(viewsets.ModelViewSet):
    queryset=Language.objects.all()
    serializer_class=LanguageSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,) #use this var name only

class ParadigmView(viewsets.ModelViewSet):
    queryset=Paradigm.objects.all()
    serializer_class=ParadigmSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)

def list(request):
    all=Language.objects.all().order_by('name')
    paginator=Paginator(all,1)
    page_number=request.GET.get('page',1)
    page_obj=paginator.get_page(page_number)
    return render(request,'languages/list.html',{'page_obj':page_obj})

def reg(request):
    return render(request,'languages/reg.html')

#setting.py can also hold permission_classes. the classes metioned there apply to all the views.
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ]
# }

# rest_framework uses basicauthentication and sessionauthentication by default. to use a different scheme like tokenauthentication,
# we can modify the settings.py file
#include rest_framework.authtoken in the installed apps and then migrate
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
#      'DEFAULT_AUTHENTICATION_CLASSES':[
#           'rest_framework.authentication.TokenAuthentication'
#      ]
# }
#
# so when the user logs in his token has to be returned. this is done by importing obtain_auth_token view from rest_framework.authtoken.views
