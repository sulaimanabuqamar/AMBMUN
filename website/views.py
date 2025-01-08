from django.shortcuts import get_object_or_404, render, HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.conf import settings
from .models import *
from itertools import groupby
import os
import sys
import json
import mimetypes

def Home(request):
    board_members = Board.objects.all().order_by('id')
    miscs = Misc.objects.all()        
    temp = {}
    for pair in miscs.values():
        temp[pair["Key"]] = pair["Value"]
    temp.update({'board_members': board_members})
    temp["schedule"] = ScheduleEntry.objects.all().order_by("date").order_by("start_time")
    dates = []
    datelengths = [-1]
    privdates  = []
    for entry in temp["schedule"].order_by("date"):
        if entry.date not in privdates:
            # date = []
            # for ent in temp["schedule"]:
            #     if ent.date == entry.date:
            #         date.append(ent)
            dates.append(entry)
            privdates.append(entry.date)
    temp["scheduleDates"] = dates
    return render(request, "index.html", temp)

def Schedule(request):
    miscs = Misc.objects.all()
    print(miscs.values()[0])
    temp = {}
    for pair in miscs.values():
        temp[pair["Key"]] = pair["Value"]
    temp["schedule"] = ScheduleEntry.objects.all().order_by("date").order_by("start_time")
    dates = []
    datelengths = [-1]
    privdates  = []
    for entry in temp["schedule"]:
        if entry.date not in privdates:
            date = []
            for ent in temp["schedule"]:
                if ent.date == entry.date:
                    date.append(ent)
            dates.append(date)
            datelengths.append(len(date)-1)
            privdates.append(entry.date)
    print(datelengths)
    temp["scheduleDates"] = dates
    temp["scheduleDateLengths"] = datelengths
    return render(request, "schedule.html", temp)

def Rules(request):
    return render(request, "rules.html")

def Committees(request):
    chairs = Chair.objects.all()
    committees = Committee.objects.all()

    context = {
        'chairs': chairs,
        'committees': committees,
    }

    return render(request, 'committees.html', context)

def Gallery(request):
    albums = Album.objects.all()

    context = {
        'albums': albums,
    }

    return render(request, 'gallery.html', context)

def Album_View(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    media_items = []
    for media_item in MediaItem.objects.all():
        if media_item.album == album:
            media_items.append(media_item)
    return render(request, 'album.html', {'album': album,'media_items':media_items, 'iterator': range(len(media_items))})
def Album_Json(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    media_items = []
    for media_item in MediaItem.objects.all():
        if media_item.album == album:
            media_items.append({'album': {'album_description': media_item.album.album_description, 'album_name': media_item.album.album_name, 'cover_photo': media_item.album.cover_photo.url, 'id': media_item.album.id}, 'id': media_item.id, 'photo': media_item.photo.url, 'video': media_item.video, 'media_type': media_item.media_type, 'description': media_item.description, 'description_visibility': media_item.description_visibility})
    return HttpResponse(json.dumps({'album': {'album_description': album.album_description, 'album_name': album.album_name, 'cover_photo': album.cover_photo.url, 'id': album.id},'media_items':media_items}))

def Committee_Detail(request, committee_id):
    committee = get_object_or_404(Committee, pk=committee_id)
    return render(request, 'committee_detail.html', {'committee': committee})

def About(request):
    return render(request, "about.html")

def Contact(request):
    board_members = Board.objects.all()
    return render(request, "contact.html", {'board_members': board_members})

def Faq(request):
    questions = FAQ.objects.all()
    return render(request, "faq.html", {'questions': questions})

@csrf_exempt
def Editor(request: WSGIRequest):
    if request.method == "GET":
        return HttpResponse("<form action='/Editor/' method='POST'><input type='text' name='username'><input type=password name=password><input type=submit></form>")
    else:
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            return render(request, "editor.html", {"starting_path": settings.BASE_DIR})
        else:
            return HttpResponse("Unauthorized Access<br><a href='/Editor'><button>Retry</button></a>", status=403)
def getFSEntryType(path):
    if os.path.isdir(path):
        return "folder"
    else:
        return "file"
def listDir(request): 
    dir = request.headers["path"]
    print(dir)
    if dir == "":
        dir = str(settings.BASE_DIR) + "/" + dir
    files = os.listdir(dir)
    fsentries = []
    print(str(settings.BASE_DIR))
    if dir != str(settings.BASE_DIR) + "/" and dir != str(settings.BASE_DIR):
        fsentries.append({"name": "..", "path": os.path.abspath(os.path.join(dir, "..")), "type": getFSEntryType(os.path.abspath(os.path.join(dir, "..")))})
    for file in files:
        fsentry = {"name": file, "path": dir + "/" + file, "type": getFSEntryType(dir + "/" + file)}
        fsentries.append(fsentry)
    
    response = HttpResponse(json.dumps(fsentries))
    response.headers["Content-Type"] = "application/json"
    return response

def getFile(request: WSGIRequest):
    try:    
        with open(request.GET["path"], 'r') as f:
            file_data = f.read()
            # sending response 
            response = HttpResponse(file_data, content_type=mimetypes.guess_type(request.GET["path"]))
            response['Content-Disposition'] = 'attachment; filename="' + f.name + '"'

    except IOError:
        # handle file not exist case here
        response = HttpResponse('<h1>File not exist</h1>', status=404)

    return response
@csrf_exempt
def writeTextFile(request: WSGIRequest):
    try:    
        with open(request.headers["path"], 'w') as f:
            f.write(request.body.decode('utf-8'))
            # sending response 
        with open(request.headers["path"], 'r') as f:
            if(f.read() == request.body.decode('utf-8')):
                response = HttpResponse("File Written Successfully", status=200)
                restartServer = True
            else:
                response = HttpResponse("File Write Error", status=500)
                restartServer = False

    except IOError:
        # handle file not exist case here
        response = HttpResponse("Unknown IOError Occurred", status=500)
        restartServer = True

    if restartServer:
        os.execv(sys.executable, ['python'] + sys.argv)
    return response

@csrf_exempt
def deleteFile(request: WSGIRequest):
    if request.method == "DELETE":
        try:    
            os.remove(request.headers["path"])
            # sending response 
            response = HttpResponse("File Deleted Successfully", status=200)

        except IOError:
            # handle file not exist case here
            response = HttpResponse("Unknown IOError Occurred", status=500)
    else:
        response = HttpResponse("Error: Request sent with " + request.method + " method, to delete files, use the delete method", status=405)
    return response

@csrf_exempt
def uploadFile(request):
    if request.method == "POST":
        handle_uploaded_file(request.FILES["file"], request.headers["path"] + "/" + request.headers["name"])
        response = HttpResponse("File Uploaded Successfully", status=200)
    else:
        response = HttpResponse("Error: Request sent with " + request.method + " method, to delete files, use the delete method", status=405)
    return response

    
@csrf_exempt
def handle_uploaded_file(f, path):
    with open(path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)