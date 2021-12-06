from django.urls import path
from .views import CattleList, CattleDetail, CattleCreate, CattleUpdate, DeleteView, CustomLoginView, RegisterPage, CattleReorder, MarketPlace
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', CattleList.as_view(), name='cattles'),
    path('cattle/<int:pk>/', CattleDetail.as_view(), name='cattle'),
    #path('cattles', views.marketPlace, name='marketplace'),
    path('cattle-create/', CattleCreate.as_view(), name='cattle-create'),
    path('cattle-update/<int:pk>/', CattleUpdate.as_view(), name='cattle-update'),
    path('cattle-delete/<int:pk>/', DeleteView.as_view(), name='cattle-delete'),
    path('cattle-reorder/', CattleReorder.as_view(), name='cattle-reorder'),
]
