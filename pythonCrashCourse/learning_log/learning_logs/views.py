from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''显示所有主题'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    '''显示特定主题下的所有条目'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    '''添加新主题'''
    if request.method != 'POST':
        # 显示表单
        form = TopicForm()
    else:
        # 处理表单提交
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    return render(request, 'learning_logs/new_topic.html', {'form': form})


def new_entry(request, topic_id):
    '''添加新条目'''
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 显示表单
        form = EntryForm()
    else:
        # 处理表单提交
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)