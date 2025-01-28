from django.urls import path


from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from . import views

app_name = "login"
urlpatterns = [
    path(
        "", LoginView.as_view(template_name="login.html", next_page="/"), name="login"
    ),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("change-password/", PasswordChangeView.as_view(), name="change-password"),
    path("signup/", views.signup, name="signup"),
    path("study/", views.study, name="study"),
    path("diary/", views.diary, name="diary"),
    path("dd/", views.dd, name="dd"),
    path("diet/", views.diet, name="diet"),
    path("smoke/", views.smoke, name="smoke"),
]
