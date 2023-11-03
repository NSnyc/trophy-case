from django.shortcuts import render
from django.views.generic.edit import CreateView
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

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def trophy_index(request):
  trophies = Trophy.objects.all()
  return render(request, 'trophies/index.html', { 'trophies': trophies })

class TrophyCreate(CreateView):
  model = Trophy
  fields = ['name', 'difficulty', 'description', 'date']

def trophy_detail(request, trophy_id):
  trophy = Trophy.objects.get(id=trophy_id)
  return render(request, 'trophies/detail.html', { 'trophy': trophy })

class TrophyCreate(CreateView):
  model = Trophy
  fields = '__all__'