from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseNotFound
from PIL import Image,ImageFont,ImageDraw
import os
from datetime import date
from django.views.decorators.csrf import csrf_exempt




def Function_pdf(name="Gourav Singh",course="PY0101EN: Python Basics for Data Science",instructor="IBM"):
    today = date.today()
    img = Image.open(os.path.join(r'E:\Major\NewClone\quill_django_project\static\Certificate.jpg'))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.path.join(r'E:\Major\NewClone\quill_django_project\static\arial_regular.ttf'),60)
    font3 = ImageFont.truetype(os.path.join(r'E:\Major\NewClone\quill_django_project\static\arial_bold.ttf'),45)
    font2 = ImageFont.truetype(os.path.join(r'E:\Major\NewClone\quill_django_project\static\arial_bold.ttf'),64)
    font4 = ImageFont.truetype(os.path.join(r'E:\Major\NewClone\quill_django_project\static\arial_bold.ttf'),120)
    text = f"a course of studey offered by {instructor}, an online learning"
    text2 =f"initiative of {instructor}."
    date1 = today.strftime("%B %d, %Y")
    da = f"Issued on {date1}"
    draw.text((190,820), name, (87, 85, 82), font=font2)
    draw.text((188,1120),course,(87, 85, 82), font=font2)
    draw.text((188,1280), text, (0,0,0), font=font)
    draw.text((188,1380), text2, (0,0,0), font=font)
    draw.text((510,1780), da, (87, 85, 82), font=font3)
    draw.text((2489,265), instructor, (87, 85, 82), font=font4)
    final_data = os.path.join(r'E:\Major\NewClone\quill_django_project\media',name+'.pdf')
    img.save(final_data)
    return (f'{name}.pdf')



@csrf_exempt
def Pdf_data(request):
    name = request.POST['name']
    course = request.POST['course']
    instructor = request.POST['instructor']
    real_name =f"{name}.pdf"
    fs = FileSystemStorage()
    a1 = "mypdf.pdf"       
    fname = f'filename={a1}'
    if fs.exists(real_name):
        created_pdf = fs.open(real_name)
        response = HttpResponse(created_pdf,content_type='application/pdf')
        response['Content-Disposition'] = fname
        return response
            
    else:
        created_pdf = fs.open(Function_pdf(name,course,instructor))
        response = HttpResponse(created_pdf,content_type='application/pdf')
        response['Content-Disposition'] = fname
        return response

