

const body = document.body

// MENU
const menuButton = document.getElementById('menu')
const closeButton = document.getElementById('close')
const navbar = document.getElementById('navbar')

menuButton.addEventListener('click', (event) => {
    navbar.classList.remove('slide-out-right-100')
    navbar.classList.add('slide-in-right-100')
    body.classList.add('modal-open')
})

closeButton.addEventListener('click', (event) => {
    navbar.classList.remove('slide-in-right-100')
    navbar.classList.add('slide-out-right-100')
    body.classList.remove('modal-open')
})


// INPUTS
const inputs = document.querySelectorAll('input')
inputs.forEach(input => {

    const label = input.parentNode.children[0]

    if (input.getAttribute('required')) {
        label.innerHTML = label.innerHTML + ' <span class="fc-red">*</span>'
    }
})


// TYPES
const ul = document.getElementById('types')
if (ul) {
    for (let li of ul.children) {

        li.addEventListener('click', (event, i) => {
    
            const active = document.getElementsByClassName('active')
            if (active[0]) {
                active[0].classList.remove('active')
            }
    
            li.classList.add('active')

            type = li.getAttribute('data-value')
            localStorage.setItem('type', type)
        })
    }
}

// MAP
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -12.0914281, lng: -77.0246911 },
        zoom: 18,
        styles: 
        [
            {
                "featureType": "all",
                "elementType": "labels.text.fill",
                "stylers": [
                    {
                        "color": "#a8afbf"
                    }
                ]
            },
            {
                "featureType": "all",
                "elementType": "labels.text.stroke",
                "stylers": [
                    {
                        "visibility": "on"
                    },
                    {
                        "color": "#373d48"
                    },
                    {
                        "weight": 2
                    },
                    {
                        "gamma": "1"
                    }
                ]
            },
            {
                "featureType": "all",
                "elementType": "labels.icon",
                "stylers": [
                    {
                        "visibility": "off"
                    }
                ]
            },
            {
                "featureType": "administrative",
                "elementType": "geometry",
                "stylers": [
                    {
                        "weight": 0.6
                    },
                    {
                        "color": "#4c576f"
                    },
                    {
                        "gamma": "0"
                    }
                ]
            },
            {
                "featureType": "landscape",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#424c65"
                    },
                    {
                        "gamma": "1"
                    },
                    {
                        "weight": "10"
                    }
                ]
            },
            {
                "featureType": "poi",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#4c576f"
                    }
                ]
            },
            {
                "featureType": "poi.business",
                "elementType": "all",
                "stylers": [
                    {
                        "visibility": "on"
                    }
                ]
            },
            {
                "featureType": "poi.government",
                "elementType": "all",
                "stylers": [
                    {
                        "visibility": "on"
                    }
                ]
            },
            {
                "featureType": "poi.medical",
                "elementType": "all",
                "stylers": [
                    {
                        "visibility": "on"
                    }
                ]
            },
            {
                "featureType": "poi.park",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#424d66"
                    }
                ]
            },
            {
                "featureType": "poi.school",
                "elementType": "geometry",
                "stylers": [
                    {
                        "visibility": "on"
                    }
                ]
            },
            {
                "featureType": "road",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#37425c"
                    },
                    {
                        "lightness": "0"
                    }
                ]
            },
            {
                "featureType": "transit",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#4c576f"
                    }
                ]
            },
            {
                "featureType": "water",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#2b364f"
                    }
                ]
            }
        ]
    });
}