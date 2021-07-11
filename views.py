from django.shortcuts import render
from django.views.generic import TemplateView
from backend.chat import  bot_name,chat


class mainpage(TemplateView):
	Template_view="index.html"

	def get(self,request):
		return render(request,self.Template_view)

	def post(self,request):
		if request.method == 'POST':
			context={"bot":chat()}
			
		return render(request,self.Template_view,context)
