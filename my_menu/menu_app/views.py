from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = 'home_page.html'

class SlugPageView(TemplateView):
    template_name = 'slug_page.html'

class NamedPageView(TemplateView):
    template_name = 'named_page.html'

