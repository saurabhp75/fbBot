from .views import bview, botview
from django.urls import path, include

urlpatterns = [
    path('646e543fb9e9bf85b4f991065d9fbffe0eed20840543f50535/', bview),
    path('66d2b8f4a09cd35cb23076a1da5d51529136a3373fd570b122/', botview.as_view()),
]
