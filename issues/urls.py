from django.urls import path
from .views import (
    IssueListView,
    IssueDetailView,
    IssueCreateView,
    IssueDeleteView,
    IssueUpdateView,
    # DraftIssueListView,
    # ArchivedIssueListView,
    # PublishedIssueListView
)

urlpatterns = [
    path('', IssueListView.as_view(), name='list'),
    path('<int:pk>', IssueDetailView.as_view(), name='detail'),
    path('new/', IssueCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', IssueUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='confirm_delete'),
]