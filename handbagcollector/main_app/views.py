from django.shortcuts import render
handbags = [
  {'name': 'Rogue 25 in Colorblock with Tea Rose', 
   'price': 895, 
   'description': 'Glovetanned leather. One credit card slot. Inside snap and multifunction pockets. Zip closure, fabric and leather lining. Two open compartments.', 
   'brand': 'Coach', 
   'color': 'Brass/Bubblegum Multi', 
   'image':'https://i.imgur.com/WJkpu1S.png'},
  {'name': 'LouLou Small Chain Bag in Quilted "Y" Leather', 
   'price': 2950, 
   'description': 'Bag with font flap and magnetic snap closure. Decorated with the cassandre and Y-quilted overstitching.', 
   'brand': 'Saint Laurent', 
   'color': 'Greyish Brown', 
   'image': 'https://i.imgur.com/2f6fnZH.png'},
  {'name': 'Quilted Nappa Leather Shoulder Bag', 
   'price': 5300, 
   'description': 'A sleek, structured shape characterizes this bag made of nappa leather, which gives it a refined touch. The corners are emphasized with metal elements that create a unique play of shapes along with the all-over geometric stitching. The metal lettering logo on the flap is a signature touch.', 
   'brand': 'Prada', 
   'color': 'Black', 
   'image': 'https://i.imgur.com/QKiNOXb.png'},
  {'name': 'Medium Lady D-Lite Bag', 
   'price': 4700, 
   'description': 'The front features a \'CHRISTIAN DIOR PARIS\' signature while the pale gold-finish metal \'D.I.O.R.\' charms embellish and illuminate its silhouette. Equipped with a wide, reversible and removable embroidered shoulder strap, the medium Lady D-Lite bag can be carried by hand or worn crossbody.', 
   'brand': 'Christian Dior', 
   'color': 'Blue Multicolor Rêve d\'Infini Embroidery', 
   'image': 'https://i.imgur.com/xIMP9Cg.png'},
  {'name': 'Devotion Mini Leather Top-Handle Bag', 
   'price': 1595, 
   'description': 'This small top-handle Devotion bag comes in calfskin. Feminine and versatile, it is distinguished by the exclusive bejeweled heart fastening and the shoulder strap inspired by the techniques of high-quality jewelers.', 
   'brand': 'Dolce & Gabbana', 
   'color': 'Red', 
   'image': 'https://i.imgur.com/ozG9HID.png'},
  {'name': 'Varenne Quad XS Leather Shoulder Bag with Pearl Strap', 
   'price': 1595, 
   'description': 'A modern yet timeless choice, our Avenue shoulder bag is Italian-crafted in luxurious box leather. Unmistakably Jimmy Choo, our foldover style features a sparkling crystal-embellished bar and the signature gold-tone JC emblem. A striking leather strap with Swarovski crystal and pearls offers the final touch of distinction.', 
   'brand': 'Jimmy Choo', 
   'color': 'Smoky Blue/Light Gold', 
   'image': 'https://i.imgur.com/DRbszWr.png'},
]
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def handbags_index(request):
  return render(request, 'handbags/index.html', {
    'handbags': handbags
  })