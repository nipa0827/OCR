# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from pydoc import TextDoc
from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
from django.shortcuts import render
import csv

try:
    import Image
except ImportError:
    from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

i = 0

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            text = pytesseract.image_to_string(Image.open(newdoc.docfile), lang='eng', config='digits')

            #writing data in data.doc file
            handle = open('data.doc', 'w+')
            handle.write(text)
            handle.close()

            #writing data in data.txt file
            textFile = open('data.txt', 'w+')
            textFile.write(text)
            textFile.close()

            ll = []

            with open('data.txt', 'r') as readFile:
                rr = readFile.readline()
                ll.append(rr)

            readFile.close()

            f = open('data.doc', 'r')

            for x in f:
                ll.append(x)

            file_content = ll
            f.close()

            #writing data in data.csv file
            with open('data.csv', 'w') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(ll)
            csvFile.close()

            context = {'file_content': file_content}

            # Redirect to the document list after POST
            return render(request, 'showText.html', context)
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

#this view method is for testing
def showText(request):
    return render_to_response('base.html')


def downloadAsText(request):
    response = HttpResponse(open("data.txt", 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename=DownloadedText.txt'
    return response

def downloadAsCSV(request):
    response = HttpResponse(open("data.csv", 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename=DownloadedText.csv'
    return response

def downloadAsDOC(request):
    response = HttpResponse(open("data.doc", 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename=DownloadedText.doc'
    return response

def about(request):
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contact.html')

def home(request):
    form = DocumentForm()
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def services(request):
    return render_to_response('services.html')
