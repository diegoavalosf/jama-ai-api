from django.urls import include, path
from .views import ReportsCreate, ReportsList, ReportsDetail


urlpatterns = [
    path('create/', ReportsCreate.as_view(), name='create-customer'),
    path('', ReportsList.as_view()),
    path('<int:pk>/', ReportsDetail.as_view(), name='retrieve-customer'),
]