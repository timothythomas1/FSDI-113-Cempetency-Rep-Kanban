from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/index.html' # Subdirectory
class AboutPageView(TemplateView):
    template_name = 'pages/about.html' # Subdirectory