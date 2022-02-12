from django.shortcuts import render
import markdown
from . import util


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