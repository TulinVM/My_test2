from django.urls import path
from .views import (
    JournalListView,
    JournalDetailView,
    JournalCreateView,
    JournalUpdateViewTwo,
    JournalUpdateView,
    JournalDeleteView,
    unauthorized_index,
    #filter_journals, 
)

urlpatterns = [
    path('', unauthorized_index, name='welcome'),
    # path('', JournalListView.as_view(), name='journal_list'),
    path('journals', JournalListView.as_view(), name='journal_list'),
    path('<int:pk>/', JournalDetailView.as_view(), name='journal_detail'),
    path('create/', JournalCreateView.as_view(), name='journal_create'),
    path('<int:pk>/update/', JournalUpdateView.as_view(), name='journal_update'),
    path('<int:pk>/update_two/', JournalUpdateViewTwo.as_view(), name='journal_update_two'),
    path('<int:pk>/delete/', JournalDeleteView.as_view(), name='journal_delete'),
    # path('filter/', filter_journals, name='journal_filter'),
]
