from django.urls import path
from . import views

urlpatterns = [
    path('outputs_state/<int:board_id>/', views.etat_outputs, name='outputs_state'),
    path('output_create/', views.handle_output_create, name='output_create'),
]
