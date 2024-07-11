from django.urls import path
from . import views
# from .views import PostView

# URL config
urlpatterns = [
    path('what/', views.say_hello),
    path('', views.post_list, name='posts'),
]

# urlpatterns = [
#     path('', PostView.as_view(), name='posts'),
# ]
