from api.views.garden_views import GardenDetail
from django.urls import path
from .views.seed_views import Seeds, SeedDetail
from .views.garden_views import Gardens, GardenDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    # routes for index and create seeds
    path('seeds/', Seeds.as_view(), name='seeds'),
    # routes for show one, update and delete seed
    path('seed/<int:pk>/', SeedDetail.as_view(), name='seed_detail'),
    # routes for index and create garden
    path('gardens/', Gardens.as_view(), name='gardens'),
    # routs for show one, update and delete garden
    path('garden/<int:pk>/', GardenDetail.as_view(), name='garden_detail'),
    # routes for auth
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password')
]
