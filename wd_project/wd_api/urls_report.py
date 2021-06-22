#

from django.urls import include, path
from .views import ReportList, ReportCreate, ReportListCreate, ReportRetrieveUpdateDestroy

urlpatterns = [
    path('', ReportList.as_view(), name='list-report'),
    path('create', ReportCreate.as_view(), name='create-report'),
    path('create/', ReportCreate.as_view(), name='create-report'),
    path('<int:id>', ReportRetrieveUpdateDestroy.as_view(), name='RUD-report'),
    path('<int:id>/', ReportRetrieveUpdateDestroy.as_view(), name='RUD-report'),
]