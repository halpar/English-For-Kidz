from django.urls import path
from flashcards.views import UserCreateAPIView,UserDeleteAPIView,UserListAPIView,UserUpdateAPIView,CardListAPIView,CardCreateAPIView,CardDeleteAPIView,CardUpdateAPIView,CardCategoryCreateAPIView,CardCategoryDeleteAPIView,CardCategoryListAPIView,CardCategoryUpdateAPIView

urlpatterns = [
    path("type/", CardCategoryListAPIView.as_view(), name="cardcategory_list"),
    path("type/create/", CardCategoryCreateAPIView.as_view(), name="cardcategory_create"),
    path("type/update/<int:pk>/", CardCategoryUpdateAPIView.as_view(), name="cardcategory_update"),
    path("type/delete/<int:pk>/", CardCategoryDeleteAPIView.as_view(), name="cardcategory_delete"),
    path("create/", CardCreateAPIView.as_view(), name="card_create"),
    path("update/<int:pk>/", CardUpdateAPIView.as_view(), name="card_update"),
    path("delete/<int:pk>/", CardDeleteAPIView.as_view(), name="card_delete"),
    path("", CardListAPIView.as_view(), name="card_list"),
    path("user/", UserListAPIView.as_view(), name="user_list"),
    path("user/create/", UserCreateAPIView.as_view(), name="user_create"),
    path("user/update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
    path("user/delete/<int:pk>/", UserDeleteAPIView.as_view(), name="user_delete"),
]