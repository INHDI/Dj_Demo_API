from django.urls import path
from home import views
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API')


urlpatterns = [
    path('', views.loginPage, name='login'),
    path('api_list/', views.klee_list, name='api_list'),
    path('api_list/<int:pk>', views.klee_details, name='api'),
    path('hello/', views.HelloView.as_view(), name='hello'),

    path('api_swagger/', schema_view),


]
