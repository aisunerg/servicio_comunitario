from django.urls import path
from .views import EditProjectView, RegisterProjectView, IndexView

app_name = "biblioteca"
urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("register/", RegisterProjectView.as_view(), name="register-project"),
    path("register/<str:id>", RegisterProjectView.as_view(), name="register-project-edit"),
    path("edit/", EditProjectView.as_view(), name="edit-project"),
]
