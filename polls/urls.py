from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
	# ex: /polls/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /polls/5/
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# ex: /polls/5/results/
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	# ex: /polls/5/vote/
	path('<int:question_id>/vote/', views.vote, name='vote'),
	path('ajax/get/', views.ajax_get, name='ajaxGet'),
	path('ajax/post/', views.ajax_post, name='ajaxPost'),
	path('ajax/json/', views.ajax_json, name='ajaxJson'),
]