from django.urls import path,include
from . import views
    
app_name = 'main'

urlpatterns = [
    path('', views.home,name='home'),
    path('graph-data', views.get_graph_data,name='get_graph_data'),
    path('generate-fake', views.generate_fake, name='generate_fake')
]