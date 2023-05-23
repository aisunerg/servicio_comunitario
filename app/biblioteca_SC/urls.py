from django.urls import path
from .views import RegisterProjectView, IndexView

app_name = "biblioteca"
urlpatterns = [path("", IndexView.as_view(), name="home"), path("register/", RegisterProjectView.as_view(), name="register-project")]
