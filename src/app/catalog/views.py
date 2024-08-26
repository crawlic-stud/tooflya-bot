from django.shortcuts import render


# Create your views here.
def index(request):
    return render(
        request,
        "catalog.html",
        context={
            "items": [
                {
                    "name": "Туфля 3000",
                    "images": [
                        "https://www.worldshop.eu/medias/img/8939992219678_w1500_z_274212826/adidas-lufthansa-limited-edition-sneaker-blue.jpeg",
                        "https://www.gabor.com/cache-buster-1/thumbnails/Produkte/Schuhe/710168/997675/image-thumb__997675__product-slider-large/710168_A1.jpg",
                        "https://balenciaga.dam.kering.com/m/612ece00eb41d4be/Medium-734734W3XL11090_F.jpg?v=2",
                    ],
                },
                {
                    "name": "Туфля GEL-KAYANO 28",
                    "images": [
                        "https://www.worldshop.eu/medias/img/8939992219678_w1500_z_274212826/adidas-lufthansa-limited-edition-sneaker-blue.jpeg",
                        "https://www.gabor.com/cache-buster-1/thumbnails/Produkte/Schuhe/710168/997675/image-thumb__997675__product-slider-large/710168_A1.jpg",
                        "https://balenciaga.dam.kering.com/m/612ece00eb41d4be/Medium-734734W3XL11090_F.jpg?v=2",
                    ],
                },
                {
                    "name": "Туфля GEL-NIMBUS 24",
                    "images": [
                        "https://www.worldshop.eu/medias/img/8939992219678_w1500_z_274212826/adidas-lufthansa-limited-edition-sneaker-blue.jpeg",
                        "https://www.gabor.com/cache-buster-1/thumbnails/Produkte/Schuhe/710168/997675/image-thumb__997675__product-slider-large/710168_A1.jpg",
                        "https://balenciaga.dam.kering.com/m/612ece00eb41d4be/Medium-734734W3XL11090_F.jpg?v=2",
                    ],
                },
                {
                    "name": "Туфля GEL-CUMULUS 24",
                    "images": [
                        "https://www.worldshop.eu/medias/img/8939992219678_w1500_z_274212826/adidas-lufthansa-limited-edition-sneaker-blue.jpeg",
                        "https://www.gabor.com/cache-buster-1/thumbnails/Produkte/Schuhe/710168/997675/image-thumb__997675__product-slider-large/710168_A1.jpg",
                        "https://balenciaga.dam.kering.com/m/612ece00eb41d4be/Medium-734734W3XL11090_F.jpg?v=2",
                    ],
                },
                {
                    "name": "Туфля GEL-CONTEND 7",
                    "images": [
                        "https://www.worldshop.eu/medias/img/8939992219678_w1500_z_274212826/adidas-lufthansa-limited-edition-sneaker-blue.jpeg",
                        "https://www.gabor.com/cache-buster-1/thumbnails/Produkte/Schuhe/710168/997675/image-thumb__997675__product-slider-large/710168_A1.jpg",
                        "https://balenciaga.dam.kering.com/m/612ece00eb41d4be/Medium-734734W3XL11090_F.jpg?v=2",
                    ],
                },
                {
                    "name": "Туфля GEL-EXCITE 9",
                    "images": [
                        "https://www.worldshop.eu/medias/img/8939992219678_w1500_z_274212826/adidas-lufthansa-limited-edition-sneaker-blue.jpeg",
                        "https://www.gabor.com/cache-buster-1/thumbnails/Produkte/Schuhe/710168/997675/image-thumb__997675__product-slider-large/710168_A1.jpg",
                        "https://balenciaga.dam.kering.com/m/612ece00eb41d4be/Medium-734734W3XL11090_F.jpg?v=2",
                    ],
                },
            ]
            * 10
        },
    )
