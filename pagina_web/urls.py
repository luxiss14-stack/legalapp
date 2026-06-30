from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Client
    path(
        "clients/register/",
        views.register_client,
        name="register_client",
    ),
    path(
        "clients/",
        views.client_list,
        name="client_list",
    ),
    path(
        "clients/<int:client_id>/",
        views.client_detail,
        name="client_detail",
    ),

    # Lawyer
    path(
        "lawyers/register/",
        views.register_lawyer,
        name="register_lawyer",
    ),
    path(
        "lawyers/",
        views.lawyer_list,
        name="lawyer_list",
    ),

    # Issues
    path(
        "clients/<int:client_id>/issue/new/",
        views.create_issue,
        name="create_issue",
    ),
    path(
        "issue/<int:issue_id>/",
        views.issue_detail,
        name="issue_detail",
    ),

    # Chat
    path(
        "issue/<int:issue_id>/chat/lawyer/<int:lawyer_id>/",
        views.lawyer_chat,
        name="lawyer_chat",
    ),
    path(
        "issue/<int:issue_id>/chat/client/",
        views.client_chat,
        name="client_chat",
    ),
]
