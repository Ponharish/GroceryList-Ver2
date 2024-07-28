from django.shortcuts import render, redirect

# Create your views here.
from createlist.models import GroceriesTable
from django.views.decorators.cache import never_cache


# Create your views here.

def printlistmenu(request):
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
        return redirect('redirectintermediateprintlist')
    return render(request, 'printlistmenu.html')

def redirectintermediateprintlist(request):
    if request.session.get('CurrentListData')['selected_list'] == 'List1':
        return redirect('printlistformlist1')
    elif request.session.get('CurrentListData')['selected_list'] == 'List2':
        return redirect('printlistformlist2')
    return render(request, 'redirectintermediatecreatelist.html')

@never_cache
def printlistformlist1(request):
    selected_list = request.session.get('CurrentListData')['selected_list']
    selected_month = request.session.get('CurrentListData')['selected_month']
    selected_year = request.session.get('CurrentListData')['selected_year']
    grocery_instance = GroceriesTable.objects.filter(list="List1", month=selected_month, year=selected_year).first()
    
    if grocery_instance:
        groceries = {key: value for key, value in grocery_instance.grocerylist.items() if value['quantity'] not in ['0', '']}
    else:
        groceries = {}
    header = "SUBU SUBU \n\n BLK 496D, #07-532, STREET 43 \nTAMPINES\nPHONE – 93734517 / 83225025"

    context = {
        'header': header,
        'grocery_instance': grocery_instance,
        'groceries': groceries,
        'notes': grocery_instance.notes if grocery_instance else '',
        'list_name': selected_list,
        'month': selected_month,
        'year': selected_year
    }
    return render(request, 'grocery_list_detail.html', context)

@never_cache
def printlistformlist2(request):
    selected_list = request.session.get('CurrentListData')['selected_list']
    selected_month = request.session.get('CurrentListData')['selected_month']
    selected_year = request.session.get('CurrentListData')['selected_year']
    grocery_instance = GroceriesTable.objects.filter(list="List2", month=selected_month, year=selected_year).first()
    
    if grocery_instance:
        groceries = {key: value for key, value in grocery_instance.grocerylist.items() if value['quantity'] not in ['0', '']}
    else:
        groceries = {}
    header = ""

    context = {
        'header': header,
        'grocery_instance': grocery_instance,
        'groceries': groceries,
        'notes': grocery_instance.notes if grocery_instance else '',
        'list_name': selected_list,
        'month': selected_month,
        'year': selected_year
    }
    return render(request, 'grocery_list_detail2.html', context)

