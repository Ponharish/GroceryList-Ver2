from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, 'mainPage.html')

from django.http import FileResponse, HttpResponseForbidden
from django.conf import settings
import os

def download_db(request):
    # Check for user authentication or authorization if needed
    
    db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')

    if not os.path.exists(db_path):
        return HttpResponseForbidden("Database file not found.")

    response = FileResponse(open(db_path, 'rb'), content_type='application/x-sqlite3')
    response['Content-Disposition'] = 'attachment; filename=db.sqlite3'
    return response