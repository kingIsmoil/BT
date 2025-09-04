from django.urls import path
from .views import (
    QuoteCreateView, QuoteDetailView,
    ApplicationCreateView, ApplicationDetailView
)

urlpatterns = [
    # Quotes
    path("quotes/", QuoteCreateView.as_view(), name="quote-create"),
    path("quotes/<int:pk>/", QuoteDetailView.as_view(), name="quote-detail"),

    # Applications
    path("applications/", ApplicationCreateView.as_view(), name="application-create"),
    path("applications/<int:pk>/", ApplicationDetailView.as_view(), name="application-detail"),
]
