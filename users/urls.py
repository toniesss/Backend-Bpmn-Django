from django.urls import path
from .views import AuthUserLoginView,UserListView
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #path('register/', UserList.as_view(), name='register'),
    path('login/', AuthUserLoginView.as_view(), name='login'),
    path('', UserListView.as_view(), name='login')
]