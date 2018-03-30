from rest_framework import routers
from .views import UserViewset
from django.conf.urls import url, include
from server import views

router = routers.DefaultRouter()

router.register(r'user', views.UserViewset)
router.register(r'user/get_search_user/(?P<search_user_name>\w+)/', views.UserViewset)
router.register(r'user/get_search_user/(?P<search_email>\w+)/', views.UserViewset)
router.register(r'user/get_search_user/(?P<search_developer>\w+)/', views.UserViewset)
#router.register(r'user/get_search_user/(?P<search_python>\w+)/', views.UserViewset)
#router.register(r'user/get_search_user/(?P<search_java>\w+)/', views.UserViewset)
#router.register(r'user/get_search_user/(?P<search_standard_c>\w+)/', views.UserViewset)
#router.register(r'user/get_search_user/(?P<search_c_plus_plus>\w+)/', views.UserViewset)
#router.register(r'user/get_search_user/(?P<search_other_language>\w+)/', views.UserViewset)

router.register(r'portfolio', views.PortfoliotView)

router.register(r'project', views.ProjectView)
router.register(r'project/get_search_proj/(?P<search_proj_name>\w+)/', views.ProjectView)
router.register(r'project/get_search_proj/(?P<search_user_projs>\w+)/', views.ProjectView)


urlpatterns = router.urls

#To test:
#http://127.0.0.1:8000/codein/user/get_search_user/?search_user_name=maryoom
#http://127.0.0.1:8000/codein/user/get_search_user/?search_email=samaher@hotmail.com
#http://127.0.0.1:8000/codein/project/get_search_proj/?search_proj_name=Bank


#http://127.0.0.1:8000/codein/user/get_search_user/?search_developer=1 XXX
#http://127.0.0.1:8000/codein/user/get_search_user/?search_java= XXX
#http://127.0.0.1:8000/codein/user/get_search_user/?search_python= XXX
#http://127.0.0.1:8000/codein/user/get_search_user/?search_c_plus_plus= XXX
#http://127.0.0.1:8000/codein/user/get_search_user/?search_standard_c= XXX
#http://127.0.0.1:8000/codein/user/get_search_user/?search_other_language= XXX

#http://127.0.0.1:8000/codein/project/get_search_proj/?search_user_projs=iii XXX
