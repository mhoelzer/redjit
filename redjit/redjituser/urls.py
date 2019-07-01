from django.urls import path
from reddit.views import SignUp, Login, Logout

urlpatterns = [
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('signup/', SignUp.as_view()),
]

