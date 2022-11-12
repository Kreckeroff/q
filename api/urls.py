from django.urls import path, include
from . import views

urlpatterns = [
    path('ConfView/<str:Title>/<str:ConfDate>/<str:ConfTag>', views.ConfView.as_view()),
    path('AddConfView/<str:Title>/<str:ConfDate>/<str:ConfTag>', views.AddConfView.as_view()),
    path('getConfView/<str:Title>/<str:ConfDate>/<str:ConfTag>',views.getConfView.as_view())
]

