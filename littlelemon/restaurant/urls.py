from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home, name='home'),
  path('menu/', views.MenuItemsView.as_view()),
  path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
  path('bookings/', views.BookingsView.as_view()),
  path('bookings/<int:pk>', views.SingleBookingView.as_view()),
]