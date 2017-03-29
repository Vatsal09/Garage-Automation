from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
#	return HttpResponse("This is the manager's page.")
#	a = HttpResponse(".")
	template = loader.get_template('pageone.html')
	context={"<p>This is the URL for second page:</p>"}
	return HttpResponse(template.render(request))
	#	return render(request, 'pageone.html')


