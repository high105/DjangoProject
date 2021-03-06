from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Player, User, Report

class IndexView(generic.ListView):
    template_name = 'ucp/index.html'
    context_object_name = 'displayUsers'
    def get_queryset(self):
        return Player.objects.order_by('id')
        
class UserView(generic.DetailView):
    model = User
    template_name = 'ucp/user.html'
    
class ReportsView(generic.DetailView):
    model = Report
    template_name = 'ucp/reports.html'
    
@property
def report_list(self):
    object_list = Report.objects.count()
    return render(self, 'ucp/user.html', { 'object_list': object_list })