#

from django.urls import include, path
from .views import ZoneListCreate, ZoneList, ZoneCreate, ZoneRetrieveUpdateDestroy, ZoneDetail, ZoneUpdate, ZoneDelete

urlpatterns = [
    path('lc', ZoneListCreate.as_view(), name='list-create-zone'),
    path('', ZoneList.as_view()),
    path('create', ZoneCreate.as_view()),
    path('create/', ZoneCreate.as_view()),
    path('<int:id>', ZoneRetrieveUpdateDestroy.as_view(), name='rud-zone'),
    path('<int:id>/', ZoneRetrieveUpdateDestroy.as_view(), name='rud-zone'),

    #path('<int:id>', ZoneDetail.as_view(), name='retrieve-zone'),
    #path('<int:id>', ZoneUpdate.as_view(), name='update-zone'),
    #path('<int:id>', ZoneDelete.as_view(), name='delete-zone'),
]