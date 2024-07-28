
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import GroceriesTable
from .groceryform1 import GroceryForm1
from .groceryform2 import GroceryForm2
from .grocerylist1 import GROCERIES_1
from .grocerylist2 import GROCERIES_2

# Create your views here.

def createlistmenu(request):
    if request.method == "POST":
        selected_list = request.POST.get('list')
        selected_month = request.POST.get('month')
        selected_year = request.POST.get('year')
        CurrentListData = {
            'selected_list':selected_list,
            'selected_month':selected_month,
            'selected_year':selected_year
        }
        request.session['CurrentListData'] = CurrentListData
        return redirect('redirectintermediatecreatelist')
    return render(request, 'createlistmenu.html')

def redirectintermediatecreatelist(request):
    if request.session.get('CurrentListData')['selected_list'] == 'List1':
        return redirect('createlistformlist1')
    elif request.session.get('CurrentListData')['selected_list'] == 'List2':
        return redirect('createlistformlist2')
    return render(request, 'redirectintermediatecreatelist.html')

def createlistformlist1(request):
    selected_list = request.session.get('CurrentListData')['selected_list']
    selected_month = request.session.get('CurrentListData')['selected_month']
    selected_year = request.session.get('CurrentListData')['selected_year']

    grocery_instance = GroceriesTable.objects.filter(list = "List1", month=selected_month, year = selected_year).first()

    if grocery_instance:
        initial_data = {f'{key}_quantity': value['quantity'] for key, value in grocery_instance.grocerylist.items()}
        initial_data['notes'] = grocery_instance.notes
        form = GroceryForm1(initial=initial_data)
    else:
        initial_data = {f'{key}_quantity': value['quantity'] for key, value in GROCERIES_1.items()}
        form = GroceryForm1(initial=initial_data)
    
    if request.method == 'POST':
        form = GroceryForm1(request.POST)
        if form.is_valid():
            groceries_data = {}
            notes = form.cleaned_data.pop('notes', '')
            for key, value in form.cleaned_data.items():
                
                item_key = key.rsplit('_', 1)[0]
                groceries_data[item_key] = {
                    'english_name': GROCERIES_1[item_key]['english_name'],
                    'tamil_name': GROCERIES_1[item_key]['tamil_name'],
                    'quantity': value
                }
                
            if grocery_instance:
                grocery_instance.grocerylist = groceries_data
                grocery_instance.notes = notes
            else:
                grocery_instance = GroceriesTable(list = "List1", month=selected_month, year = selected_year, grocerylist=groceries_data, notes=notes)
            grocery_instance.save()
            return redirect('acknowledgeceeation')
    
    return render(request, 'grocery_form_list_1.html', {'form': form, 'groceries': GROCERIES_1})

def acknowledgeceeation(request):
    request.session.pop('CurrentListData')
    return render(request, "acknowledgeceeation.html")


def createlistformlist2(request):
    selected_list = request.session.get('CurrentListData')['selected_list']
    selected_month = request.session.get('CurrentListData')['selected_month']
    selected_year = request.session.get('CurrentListData')['selected_year']

    grocery_instance = GroceriesTable.objects.filter(list = "List2", month=selected_month, year = selected_year).first()

    if grocery_instance:
        initial_data = {f'{key}_quantity': value['quantity'] for key, value in grocery_instance.grocerylist.items()}
        initial_data['notes'] = grocery_instance.notes
        form = GroceryForm2(initial=initial_data)
    else:
        initial_data = {f'{key}_quantity': value['quantity'] for key, value in GROCERIES_2.items()}
        form = GroceryForm2(initial=initial_data)
    
    if request.method == 'POST':
        form = GroceryForm2(request.POST)
        if form.is_valid():
            groceries_data = {}
            notes = form.cleaned_data.pop('notes', '')
            for key, value in form.cleaned_data.items():
                
                item_key = key.rsplit('_', 1)[0]
                groceries_data[item_key] = {
                    'english_name': GROCERIES_2[item_key]['english_name'],
                    'tamil_name': GROCERIES_2[item_key]['tamil_name'],
                    'quantity': value
                }
                
            if grocery_instance:
                grocery_instance.grocerylist = groceries_data
                grocery_instance.notes = notes
            else:
                grocery_instance = GroceriesTable(list = "List2", month=selected_month, year = selected_year, grocerylist=groceries_data, notes=notes)
            grocery_instance.save()
            return redirect('acknowledgeceeation')
    
    return render(request, 'grocery_form_list_2.html', {'form': form, 'groceries': GROCERIES_2})