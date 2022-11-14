from django.urls import path, include
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('ConfView/<str:Title>/<str:ConfDate>/<str:ConfTag>', views.ConfView.as_view()),
    path('AddConfView/<str:Title>/<str:ConfDate>/<str:ConfTag>', views.AddConfView.as_view()),
    path('getConfView/<str:Title>/<str:ConfDate>/<str:ConfTag>', views.getConfView.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",),
]

