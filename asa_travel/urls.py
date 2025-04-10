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
    path('my_reviews/',views.my_reviews,name='my_reviews')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)