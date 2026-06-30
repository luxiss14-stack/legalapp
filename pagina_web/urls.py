from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

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
    path(
        "chat/<int:issue_id>/send/",
        views.send_chat_message,
        name="send_chat_message",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="pagina_web/login.html",
            authentication_form=LoginForm,
            redirect_authenticated_user=True,
        ),
        name="login",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
]
