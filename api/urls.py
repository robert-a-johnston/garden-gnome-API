from api.views.garden_views import GardenDetail
from django.urls import path
from .views.seed_views import Seeds, SeedDetail
from .views.garden_views import Gardens, GardenDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('seeds/', Seeds.as_view(), name='seeds'),
    path('seeds/<int:pk>/', SeedDetail.as_view(), name='seed_detail'),
    path('gardens/', Gardens.as_view(), name='gardens'),
    path('gardens/<int:pk>/', GardenDetail.as_view(), name='garden_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
