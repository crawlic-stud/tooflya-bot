from django.shortcuts import render


# Create your views here.
def index(request):
    return render(
        request,
        "catalog.html",
        context={
            "items": [
                {"name": "Туфля 3000"},
                {"name": "Туфля GEL-KAYANO 28"},
                {"name": "Туфля GEL-NIMBUS 24"},
                {"name": "Туфля GEL-CUMULUS 24"},
                {"name": "Туфля GEL-CONTEND 7"},
                {"name": "Туфля GEL-EXCITE 9"},
                {"name": "Туфля GEL-FLUX 5"},
                {"name": "Туфля GEL-QUANTUM 360 6"},
                {"name": "Туфля GEL-PULSE 13"},
                {"name": "Туфля GEL-VENTURE 8"},
            ]
            * 10
        },
    )
