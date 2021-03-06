from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Question, Choice

# Create your views here.


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""
		Return the last five published questions.(not including those set to
		be published in the future)
		less than or equal to - that is, earlier than or equal to - timezone.now
		"""
		return Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		:return:
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


def vote(request, question_id):
	# 竞争条件问题
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def ajax_get(request):
	return HttpResponse(str(request.GET))


@csrf_exempt
def ajax_post(request):
	question = get_object_or_404(Question, pk=request.POST['id'])
	return HttpResponse(question)


# csrf_exempt是告诉你的视图不要检查csrf 标记
@csrf_exempt
def ajax_json(request):
	question = get_object_or_404(Question, pk=request.POST['id'])
	choice_list = serializers.serialize("json", question.choice_set.all())
	print(choice_list)
	return HttpResponse(choice_list, content_type='application/json')