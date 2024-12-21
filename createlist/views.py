
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import GroceriesTable
from .groceryform1_fields import load_master_fields_1
from .groceryform2_fields import load_master_fields_2
from .formGenerator import GroceryForm


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

    fields_to_add_1 = load_master_fields_1()
    if grocery_instance:
        initial_data = {f'{key}': value['quantity'] for key, value in grocery_instance.grocerylist.items() if key != 'notes'}
        initial_data['notes'] = grocery_instance.notes
        form = GroceryForm(initial=initial_data, fields_to_add=fields_to_add_1)
    else:
        initial_data = {f'{key}': value['quantity'] for key, value in fields_to_add_1.items() if key != 'notes'}
        form = GroceryForm(initial=initial_data, fields_to_add=fields_to_add_1)
    
    if request.method == 'POST':
        form = GroceryForm(request.POST, fields_to_add=fields_to_add_1)
        if form.is_valid():
            groceries_data = {}
            notes = form.cleaned_data.pop('notes', '')
            for key, value in form.cleaned_data.items():
                
                item_key = key.rsplit('_', 1)[0]
                if value not in ['0', '']:
                    groceries_data[item_key] = {
                        'english_name': fields_to_add_1[item_key]['english_name'],
                        'tamil_name': fields_to_add_1[item_key]['tamil_name'],
                        'quantity': value
                    }
                
            if grocery_instance:
                grocery_instance.grocerylist = groceries_data
                grocery_instance.notes = notes
            else:
                grocery_instance = GroceriesTable(list = "List1", month=selected_month, year = selected_year, grocerylist=groceries_data, notes=notes)
            grocery_instance.save()
            return redirect('acknowledgeceeation')

    return render(request, "grocery_form_list_1.html", {"form": form, 'fieldNames': form.fieldNames})

def createlistformlist2(request):
    selected_list = request.session.get('CurrentListData')['selected_list']
    selected_month = request.session.get('CurrentListData')['selected_month']
    selected_year = request.session.get('CurrentListData')['selected_year']

    grocery_instance = GroceriesTable.objects.filter(list = "List2", month=selected_month, year = selected_year).first()
    fields_to_add_2 = load_master_fields_2()
    if grocery_instance:
        #The below is also recording the field notes - remove that field!!
        initial_data = {f'{key}': value['quantity'] for key, value in grocery_instance.grocerylist.items() if key != 'notes'}
        initial_data['notes'] = grocery_instance.notes
        form = GroceryForm(initial=initial_data, fields_to_add=fields_to_add_2)
    else:
        initial_data = {f'{key}': value['quantity'] for key, value in fields_to_add_2.items() if key != 'notes'}
        form = GroceryForm(initial=initial_data, fields_to_add=fields_to_add_2)
    
    if request.method == 'POST':
        form = GroceryForm(request.POST, fields_to_add=fields_to_add_2)
        if form.is_valid():
            groceries_data = {}
            notes = form.cleaned_data.pop('notes', '')
            for key, value in form.cleaned_data.items():
                
                item_key = key.rsplit('_', 1)[0]
                if value not in ['0', '']:
                    groceries_data[item_key] = {
                        'english_name': fields_to_add_2[item_key]['english_name'],
                        'tamil_name': fields_to_add_2[item_key]['tamil_name'],
                        'quantity': value
                    }
                
            if grocery_instance:
                grocery_instance.grocerylist = groceries_data
                grocery_instance.notes = notes
            else:
                grocery_instance = GroceriesTable(list = "List2", month=selected_month, year = selected_year, grocerylist=groceries_data, notes=notes)
            grocery_instance.save()
            return redirect('acknowledgeceeation')
    
    return render(request, 'grocery_form_list_2.html', {"form": form, 'fieldNames': form.fieldNames})

def acknowledgeceeation(request):
    request.session.pop('CurrentListData')
    return render(request, "acknowledgeceeation.html")
