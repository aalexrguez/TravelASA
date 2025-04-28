from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'asa_travel'

urlpatterns = [
    path('',views.index),
    path('home/',views.index),
    path('destination_detail/<int:destination_id>',views.destination_detail,name='destination_detail'),
    path('accounts/register/',views.registration,name='register'),
    path('review/',views.review,name='review'),
    path('my_reviews/',views.my_reviews,name='my_reviews'),
    path('update_review/<int:review_id>',views.update_review,name='update_review'),
    path('delete_review/<int:review_id>',views.delete_review,name='delete_review'),
    path('attraction/<int:destination_id>',views.attraction,name='attraction'),
    path('activities/<int:destination_id>',views.activities,name='activities'),
    path('restaurant/<int:restaurant_id>',views.restaurant,name='restaurant'),
    path('accommodation/<int:accommodation_id>',views.accommodation,name='accommodation'),
    path('edit_attraction/<int:attraction_id>',views.edit_attraction,name='edit_attraction'),
    path('edit_restaurant/<int:restaurant_id>',views.edit_restaurant,name='edit_restaurant'),
    path('edit_accomodation<int:accommodation_id>',views.edit_accommodation,name='edit_accommodation'),
    path('edit_activity/<int:activity_id>',views.edit_activity,name='edit_activity'),
    path('review_delete/<int:review_id>',views.delete_review,name='delete_review'),
    path('delete_attraction/<int:attraction_id>',views.delete_attraction,name='delete_attraction'),
    path('delete_restaurant/<int:restaurant_id>',views.delete_restaurant,name='delete_restaurant'),
    path('delete_accommodation/<int:accommodation_id>',views.delete_accommodation,name='delete_accommodation'),
    path('delete_activity/<int:activity_id>',views.delete_activity,name='delete_activity')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)