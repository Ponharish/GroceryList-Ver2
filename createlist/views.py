import os
import pyodbc

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
            grocery_instance[heading] = str(row[2])
        TableExistsFlag = True
    except pyodbc.ProgrammingError:
        #Table does not exist
        pass

    cursor.close() 
    conn.close()

    fields_to_add_1 = load_master_fields_1()

    if TableExistsFlag:
        initial_data = {f'{key}': f'{value}' for key, value in grocery_instance.items() if key != 'notes'}
        initial_data['notes'] = grocery_instance['notes']
        form = GroceryForm(initial=initial_data, fields_to_add=fields_to_add_1)
    else:
        initial_data = {f'{key}': value['quantity'] for key, value in fields_to_add_1.items() if key != 'notes'}
        form = GroceryForm(initial=initial_data, fields_to_add=fields_to_add_1)

    if request.method == 'POST':
        form = GroceryForm(request.POST, fields_to_add=fields_to_add_1)
        if form.is_valid():
            groceries_data = {}
            data = []

            notes = form.cleaned_data.pop('notes', '')
            for key, value in form.cleaned_data.items():
                
                item_key = key.rsplit('_', 1)[0]
                if value not in ['0', '']:
                    curr = (fields_to_add_1[item_key]['english_name'], 
                            fields_to_add_1[item_key]['tamil_name'],
                            value)
                    data.append(curr)
            data.append(('notes','', notes))
            if TableExistsFlag:
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

                cursor.execute(f"DELETE FROM Groceries.{ListIdentifier};")
                conn.commit()
                insert_sql = f"""
                INSERT INTO Groceries.{ListIdentifier}
                VALUES (?, ?, ?);
                """
                cursor.executemany(insert_sql, data)
                conn.commit()
                cursor.close()
                conn.close()
            else:
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

                create_table_sql = f"""
                CREATE TABLE Groceries.{ListIdentifier} (
                    english_name VARCHAR(100) NOT NULL,
                    tamil_name NVARCHAR(100),
                    quantity VARCHAR(1200),
                    id INT IDENTITY(1,1) PRIMARY KEY
                );
                """
                cursor.execute(create_table_sql)
                conn.commit()
                insert_sql = f"""
                INSERT INTO Groceries.{ListIdentifier}
                VALUES (?, ?, ?);
                """
                cursor.executemany(insert_sql, data)
                conn.commit()
                cursor.close()
                conn.close()
            return redirect('acknowledgeceeation')

    return render(request, "grocery_form_list_1.html", {"form": form, 'fieldNames': form.fieldNames})



def createlistformlist2(request):
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
            grocery_instance[heading] = str(row[2])
        TableExistsFlag = True
    except pyodbc.ProgrammingError:
        #Table does not exist
        pass
    cursor.close() 
    conn.close() 

    fields_to_add_2 = load_master_fields_2() 

    if TableExistsFlag:
        initial_data = {f'{key}': f'{value}' for key, value in grocery_instance.items() if key != 'notes'}
        initial_data['notes'] = grocery_instance['notes']
        form = GroceryForm(initial=initial_data, fields_to_add=fields_to_add_2)
    else:
        initial_data = {f'{key}': value['quantity'] for key, value in fields_to_add_2.items() if key != 'notes'}
        form = GroceryForm(initial=initial_data, fields_to_add=fields_to_add_2)


    if request.method == 'POST':
        form = GroceryForm(request.POST, fields_to_add=fields_to_add_2)
        if form.is_valid():
            data = []
            notes = form.cleaned_data.pop('notes', '')
            for key, value in form.cleaned_data.items():
                item_key = key.rsplit('_', 1)[0]
                if value not in ['0', '']:
                    curr = (fields_to_add_2[item_key]['english_name'], 
                            fields_to_add_2[item_key]['tamil_name'],
                            value)
                    data.append(curr)
            data.append(('notes','', notes))
            if TableExistsFlag:
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

                cursor.execute(f"DELETE FROM Groceries.{ListIdentifier};")
                conn.commit()
                insert_sql = f"""
                INSERT INTO Groceries.{ListIdentifier}
                VALUES (?, ?, ?);
                """
                cursor.executemany(insert_sql, data)
                conn.commit()
                cursor.close()
                conn.close()

            else:
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

                create_table_sql = f"""
                CREATE TABLE Groceries.{ListIdentifier} (
                    english_name VARCHAR(100) NOT NULL,
                    tamil_name NVARCHAR(100),
                    quantity VARCHAR(1200),
                    id INT IDENTITY(1,1) PRIMARY KEY
                );
                """
                cursor.execute(create_table_sql)
                conn.commit()

                insert_sql = f"""
                INSERT INTO Groceries.{ListIdentifier}
                VALUES (?, ?, ?);
                """
                cursor.executemany(insert_sql, data)
                conn.commit()
                cursor.close()
                conn.close()

            return redirect('acknowledgeceeation')
    return render(request, 'grocery_form_list_2.html', {"form": form, 'fieldNames': form.fieldNames})

def acknowledgeceeation(request):
    request.session.pop('CurrentListData')
    return render(request, "acknowledgeceeation.html")
