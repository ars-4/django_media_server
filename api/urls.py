from api import views
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('person', views.PersonViewSet)
router.register('actor', views.ActorViewSet)
router.register('tag', views.TagViewSet)
router.register('movie', views.MovieViewSet)
router.register('receipts', views.BillReceiptViewSet)


urlpatterns = [

    path('', include(router.urls)),

    path('auth/register/', views.RegisterView.as_view()),
    path('auth/login/', views.LoginView.as_view()),

    path('token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', views.TokenVerifyView.as_view(), name='token_verify'),

]
