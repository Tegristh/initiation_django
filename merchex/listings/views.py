from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, 
                  "listings/hello.html",
                  context={"bands": bands}
                  )


def about(request):
    return render(request, "listings/about.html")

def listing(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html",
                  context={"elements":listings}
                  )

def contact(request):
    return render(request, "listings/contact.html")
