from django.views.generic import TemplateView

class IndexPageView(TemplateView):
	template_name = 'index.html'



class AboutPageView(TemplateView):
	template_name = 'about.html'
		

class ContactPageView(TemplateView):
	template_name = 'contact.html'