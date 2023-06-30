from django.contrib import admin
from django.urls import path
from . import views
app_name = 'foodapp'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('food/<int:food_id>/', views.details, name='details'),
    path('add/', views.adding, name='adding'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
  ]
