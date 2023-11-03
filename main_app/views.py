from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Trophy


# class Trophy:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, difficulty, description, date):
#     self.name = name
#     self.difficulty = difficulty
#     self.description = description
#     self.date = date

# trophies = [
#   Trophy('Lolo', 1, 'Kinda rude.', '3/3/2023'),
#   Trophy('Sachi', 2, 'Looks like a turtle.', '3/3/2023'),
#   Trophy('Fancy', 3, 'Happy fluff ball.', '3/3/2023'),
#   Trophy('Bonk', 4, 'Meows loudly.', '3/3/2023')
# ]

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def trophy_index(request):
  trophies = Trophy.objects.filter(user=request.user)
  return render(request, 'trophies/index.html', { 'trophies': trophies })

class TrophyCreate(LoginRequiredMixin, CreateView):
  model = Trophy
  fields = ['name', 'difficulty', 'description', 'date']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required
def trophy_detail(request, trophy_id):
  trophy = Trophy.objects.get(id=trophy_id)
  return render(request, 'trophies/detail.html', { 'trophy': trophy })

class TrophyCreate(LoginRequiredMixin, CreateView):
  model = Trophy
  fields = '__all__'

class TrophyUpdate(LoginRequiredMixin, UpdateView):
  model = Trophy
  fields = ['difficulty', 'description', 'date']

class TrophyDelete(LoginRequiredMixin, DeleteView):
  model = Trophy
  success_url = '/trophies/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)