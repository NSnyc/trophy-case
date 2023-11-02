from django.shortcuts import render


class Trophy:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, difficulty, description, completion_date):
    self.name = name
    self.difficulty = difficulty
    self.description = description
    self.completion_date = completion_date

trophies = [
  Trophy('Lolo', 1, 'Kinda rude.', 3/3/2023),
  Trophy('Sachi', 2, 'Looks like a turtle.', 3/3/2023),
  Trophy('Fancy', 3, 'Happy fluff ball.', 3/3/2023),
  Trophy('Bonk', 4, 'Meows loudly.', 3/3/2023)
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def trophy_index(request):
  return render(request, 'trophies/index.html', { 'trophies': trophies })