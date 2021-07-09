from django.shortcuts import render
from django.views.generic import TemplateView


class mainpage(TemplateView):
	Template_view="index.html"

	def get(self,request):
		return render(request,self.Template_view)
