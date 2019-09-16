from django.conf.appUrls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from portalApp.views import views
from portalApp.views.api import GenericModelController


urlpatterns = [
    url(r'^$', views.home),

    url(r'^api/', include([
        url(r'^model/', GenericModelController.as_view()),
    ])),

    url(r'^dashboard/', views.dashboard),
    url(r'^delete_model/', views.delete_model),
]
