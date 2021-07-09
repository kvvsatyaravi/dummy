
from django.shortcuts import render
from django.views.generic import TemplateView
from kittu.models import funday

class Homeview(TemplateView):
	Template_view="sample.html"

	def get(self,request):
		return render(request,self.Template_view)

	def post(self,request):
		if request.method == 'POST':
			num=request.POST.get('input',None)
		context={'data':funday.objects.get(idnum=num)}
		return render(request,self.Template_view,context)