from django.urls import path

from . import views


urlpatterns = [
    path("",views.ReviewView.as_view()),
    path("thank-you",views.ThankyouView.as_view()),
    path("listing",views.ReviewlistView.as_view()),
    path("listing/favourites",views.AddfavouriteView.as_view()),
    path("listing/<int:pk>",views.DetailsView.as_view(),name="listview")
]
