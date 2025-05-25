from django.shortcuts import redirect
from django.shortcuts import render

import os
import pyodbc


def addToListMenu(request):
    if request.method == "POST":
        selected_list = request.POST.get('list')
        english_name = request.POST.get('english_name')
        tamil_name = request.POST.get('tamil_name')

        if '2' in selected_list:
            ListIdentifier = '2'
        elif '1' in selected_list:
            ListIdentifier = '1'

        status = True #Fail

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
        Existing_grocery = [] #a list of tuples (eng_name, tam_name)
        
        query = f"""
            SELECT * FROM Groceries.MasterList{ListIdentifier}
            WHERE LOWER(english_name) = LOWER(?)
            OR LOWER(tamil_name) = LOWER(?)
        """
        cursor.execute(query, (english_name, tamil_name))
        rows = cursor.fetchall()
        for row in rows:
            Existing_grocery.append((row[0],row[1]))
        if len(Existing_grocery) == 0:
            status = False
        cursor.close() 
        conn.close()

        if status:
            message = "\n\nThere is a clash with the following groceries: \n"
            for i in Existing_grocery:
                message += "> " + i[0] + " , " + i[1] + "\n"
            error_message = "A similar grocery exists" + message
            
            return render(request, 'addToListMenu.html', {
                'error_message': error_message,
                'selected_list': selected_list,
                'english_name': english_name,
                'tamil_name': tamil_name
            })

        CurrentListData = {
            'selected_list':selected_list,
            'english_name':english_name,
            'tamil_name':tamil_name
        }
        request.session['CurrentListToAdd'] = CurrentListData
        return redirect('addToListConfirm')
    return render(request, 'addToListMenu.html')






def addToListConfirm(request):
    selected_list = request.session.get('CurrentListToAdd')['selected_list']
    english_name = request.session.get('CurrentListToAdd')['english_name']
    tamil_name = request.session.get('CurrentListToAdd')['tamil_name']

    if request.method == "POST":
        if '2' in selected_list:
            ListIdentifier = '2'
        elif '1' in selected_list:
            ListIdentifier = '1'

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

        insert_sql = f"""
        INSERT INTO Groceries.MasterList{ListIdentifier}
        VALUES (?, ?, ?);
        """
        cursor.execute(insert_sql, (english_name, tamil_name, ''))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('ACKaddToList')    
    
    if '2' in selected_list:
        selected_list = "2  (Eruvadi)"
    elif '1' in selected_list:
        selected_list = "1  (Singapore)" 

    return render(request, "addToListConfirm.html", 
        {"selected_list": selected_list,
        'english_name': english_name,
        'tamil_name': tamil_name,
        }
    )

def ACKaddToList(request):
    request.session.pop('CurrentListToAdd')
    return render(request, "ACKaddToList.html")