from django.shortcuts import render
import markdown
from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
    t={title}
    f = util.get_entry(list(t)[0])
    if f is not None:
        html = markdown.markdown(f)
        return render(request, "encyclopedia/title.html",{
        "title": list(t)[0], "body":html
         })
    else :
        return render(request, "encyclopedia/notFound.html")


def search(request):
    searchQuery =request.GET.get('q')
    f = util.get_entry(searchQuery)
    if f is not None:
        html = markdown.markdown(f)
        return render(request, "encyclopedia/title.html",{
        "title": f, "body":html
         })
    else :
         x= util.list_subEntries(request.GET.get('q'))
         return render(request, "encyclopedia/searchResults.html", {
         "entries": util.list_subEntries(request.GET.get('q'))
         })
def newPage(request):
    return render(request, "encyclopedia/newPage.html") 
    
def newPageSave(request):
    title=request.GET.get('title')
    body=request.GET.get('markdownBody')
    f = util.get_entry(title)
    if f is not None:
       return render(request, "encyclopedia/saveError.html") 
    else:
       util.save_entry(title,body)
       newPage=util.get_entry(title)
       html = markdown.markdown(newPage)
       return render(request, "encyclopedia/title.html",{
        "title": title, "body":html
         })
    return render(request, "encyclopedia/newPage.html")

def randomPage(request):
    entries=util.list_entries()
    random_index = random.randint(0,len(entries)-1)
    entryTitle=entries[random_index]
    f = util.get_entry(entryTitle)
    html = markdown.markdown(f)
    return render(request, "encyclopedia/title.html",{
        "title": entryTitle, "body":html
         })