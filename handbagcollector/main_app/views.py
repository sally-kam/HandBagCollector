from django.shortcuts import render
handbags = [
  {'name': 'Rogue 25 in Colorblock with Tea Rose', 'price': 895, 'description': 'Glovetanned leather. One credit card slot. Inside snap and multifunction pockets. Zip closure, fabric and leather lining. Two open compartments', 'brand': 'Coach', 'color': 'Brass/Bubblegum Multi'},
  {'name': 'LOULOU SMALL CHAIN BAG IN QUILTED "Y" LEATHER', 'price': 3450, 'description': 'BAG WITH FRONT FLAP AND MAGNETIC SNAP CLOSURE DECORATED WITH THE CASSANDRE AND Y-QUILTED OVERSTITCHING.', 'brand': 'Saint Laurent', 'color': 'Greyish Brown'},
]
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')