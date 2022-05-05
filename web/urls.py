from django.urls import path
from web import views

urlpatterns = [
    path('', views.homepage, name='HomePage'),

    path('movie/<int:pk>/', views.moviepage, name='MoviePage'),
    path('moviewatchersincrement/<int:pk>/', views.moviepagewatchers),

    path('account/<int:pk>/', views.userreadpage, name='UserPage'),
    path('account/<int:pk>/update/', views.userupdatepage, name='UserUpdatePage'),

    path('useraccountmanagement/', views.usertypemanagement, name='UserAccountManagement'),
    path('useraccountmanagementform/<int:pk>/', views.usertypemanagementform, name='UserAccountManagementForm'),

    path('packages/', views.typereadpage, name='ReadPackages'),
    path('packages/create/', views.typecreatepage, name='CreatePackage'),
    path('packages/<int:pk>/update/', views.typeupdatepage, name='UpdatePackage'),
    path('packages/<int:pk>/delete/', views.typedeletepage, name='DeletePackage'),

    path('create/', views.moviecreatepage, name='CreateMovie'),

    path('actors/create/', views.actorcreatepage, name='CreateActor'),
    path('actors/<int:pk>/', views.actorreadpage, name='ReadActor'),

    path('tags/create/', views.tagcreatepage, name='CreateTag'),
]
