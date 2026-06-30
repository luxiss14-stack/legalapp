from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Lawyer, Issue
from .forms import (
    ClientRegistrationForm,
    LawyerRegistrationForm,
    IssueForm,
    ChatMessageForm,
)


def home(request):
    return render(request, "legal_app/home.html")


# -------------------------
# Client Registration
# -------------------------
def register_client(request):
    if request.method == "POST":
        form = ClientRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("client_list")

    else:
        form = ClientRegistrationForm()

    return render(
        request,
        "legal_app/register_client.html",
        {"form": form},
    )


# -------------------------
# Lawyer Registration
# -------------------------
def register_lawyer(request):
    if request.method == "POST":
        form = LawyerRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lawyer_list")

    else:
        form = LawyerRegistrationForm()

    return render(
        request,
        "legal_app/register_lawyer.html",
        {"form": form},
    )


# -------------------------
# Lists
# -------------------------
def client_list(request):
    clients = Client.objects.all()

    return render(
        request,
        "legal_app/client_list.html",
        {"clients": clients},
    )


def lawyer_list(request):
    lawyers = Lawyer.objects.all()

    return render(
        request,
        "legal_app/lawyer_list.html",
        {"lawyers": lawyers},
    )


# -------------------------
# Issues
# -------------------------
def create_issue(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == "POST":
        form = IssueForm(request.POST)

        if form.is_valid():
            issue = form.save(commit=False)
            issue.client = client
            issue.save()

            return redirect("client_detail", client.id)

    else:
        form = IssueForm()

    return render(
        request,
        "legal_app/create_issue.html",
        {
            "client": client,
            "form": form,
        },
    )


def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    return render(
        request,
        "legal_app/client_detail.html",
        {
            "client": client,
            "issues": client.issues.all(),
        },
    )


def issue_detail(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)

    return render(
        request,
        "legal_app/issue_detail.html",
        {
            "issue": issue,
            "messages": issue.messages.order_by("created_at"),
        },
    )


# -------------------------
# Chat
# -------------------------
def lawyer_chat(request, issue_id, lawyer_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    lawyer = get_object_or_404(Lawyer, pk=lawyer_id)

    if request.method == "POST":
        form = ChatMessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.issue = issue
            message.client = issue.client
            message.lawyer = lawyer
            message.sent_by_lawyer = True
            message.save()

            return redirect(
                "lawyer_chat",
                issue_id=issue.id,
                lawyer_id=lawyer.id,
            )

    else:
        form = ChatMessageForm()

    return render(
        request,
        "legal_app/chat.html",
        {
            "issue": issue,
            "lawyer": lawyer,
            "messages": issue.messages.order_by("created_at"),
            "form": form,
        },
    )


def client_chat(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)

    if request.method == "POST":
        form = ChatMessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.issue = issue
            message.client = issue.client
            message.lawyer = issue.messages.first().lawyer
            message.sent_by_lawyer = False
            message.save()

            return redirect("client_chat", issue.id)

    else:
        form = ChatMessageForm()

    return render(
        request,
        "legal_app/chat.html",
        {
            "issue": issue,
            "lawyer": issue.messages.first().lawyer if issue.messages.exists() else None,
            "messages": issue.messages.order_by("created_at"),
            "form": form,
        },
    )
