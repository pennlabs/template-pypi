from django.urls import include, path


urlpatterns = [path("", include("project_name.urls", namespace="project_name"))]
