from django.shortcuts import render, redirect

import os
import pyodbc

# Create your views here.
from createlist.models import GroceriesTable
from django.views.decorators.cache import never_cache

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

    ListIdentifier = 'List1' + '_' + selected_month + '_' + selected_year
    TableExistsFlag = False
    
    conn = pyodbc.connect(
        f"DRIVER={os.getenv('DB_DRIVER')};"
        f"SERVER={os.getenv('DB_HOST')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
    )
    cursor = conn.cursor()
    grocery_instance = {}

    try:
        cursor.execute("SELECT * FROM Groceries." + ListIdentifier)
        rows = cursor.fetchall()
        for row in rows:
            heading = ''.join(row[0].split()).lower()
            grocery_instance[heading] = {'english_name': str(row[0]),
                                         'tamil_name': str(row[1]),
                                         'quantity': str(row[2])}
        TableExistsFlag = True
    except pyodbc.ProgrammingError:
        #Table does not exist
        pass
    
    cursor.close() 
    conn.close() 

    note = ''
    if TableExistsFlag:
        note = grocery_instance['notes']['quantity']
        grocery_instance.pop('notes')
        groceries = {key: value for key, value in grocery_instance.items() if value['quantity'] not in ['0', '']}      
    else:
        groceries = {}

    header = "SUBU SUBU \n\n BLK 496D, #07-532, STREET 43 \nTAMPINES\nPHONE – 93734517 / 83225025"

    context = {
        'header': header,
        'groceries': groceries,
        'notes': note,
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

    ListIdentifier = 'List2' + '_' + selected_month + '_' + selected_year
    TableExistsFlag = False
    
    conn = pyodbc.connect(
        f"DRIVER={os.getenv('DB_DRIVER')};"
        f"SERVER={os.getenv('DB_HOST')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
    )
    cursor = conn.cursor()
    grocery_instance = {}

    try:
        cursor.execute("SELECT * FROM Groceries." + ListIdentifier)
        rows = cursor.fetchall()
        for row in rows:
            heading = ''.join(row[0].split()).lower()
            grocery_instance[heading] = {'english_name': str(row[0]),
                                         'tamil_name': str(row[1]),
                                         'quantity': str(row[2])}
        TableExistsFlag = True
    except pyodbc.ProgrammingError:
        pass
        #Table does not exist
    
    cursor.close() 
    conn.close() 

    note = ''
    if TableExistsFlag:
        note = grocery_instance['notes']['quantity']
        grocery_instance.pop('notes')
        groceries = {key: value for key, value in grocery_instance.items() if value['quantity'] not in ['0', '']}       
    else:
        groceries = {}

    header = ""
    context = {
        'header': header,
        'groceries': groceries,
        'notes': note,
        'list_name': selected_list,
        'month': selected_month,
        'year': selected_year
    }
    return render(request, 'grocery_list_detail2.html', context)

