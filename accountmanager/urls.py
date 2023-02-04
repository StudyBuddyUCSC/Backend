from django.urls import path


from .views import SignUpView



urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    #path("signup/", views.as_view(), name="signup"),
]
    