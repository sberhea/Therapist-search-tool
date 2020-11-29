"use strict"
let map;

// function initMap() {
//     // Code that works with Google Maps here
//     map = new google.maps.Map( document.querySelector('#map'),{
//         center: { lat : 44.9375 , lng: 93.2010 },
//         zoom: 11,
//     });
// (document.getElementById("map")
//   }

function initMap() {
  
  const map = new google.maps.Map( document.querySelector('#map'),{
    center: { lat: 44.9778, lng: 93.2650 },
    zoom: 8,
  }); //close base map

    // Retrieve info with AJAX
    const jsonURL = "/api/therapists";

    $.get(jsonURL, (therapists) => {
    
      for (let therapist of therapists) {
        //Define content of infoWindow
        const therapistInfoContent = (`
        <div class = "window-content">
          <div class = "t-thumbnail">
            <img src = therapist.pic">
          </div>
          
          <ul class="therapist-info">
            <li><b>Therapist name: </b>${therapist.name}</li>
          </ul>
        </div>
        `);
        
        //Create marker
        const therapistMarker = new google.maps.Marker({
          position: {
            lat: Number(therapist.latitude),
            lng: Number(therapist.longitude)
          },
          title: `Therapist ID: ${therapist.therapist_id}`,
          icon: {
            url: therapist.pic,
            scaledSize: new google.maps.Size(50,50)
          },
          map: map,
        }); //marker closed
        
        //Event listerner for when user clicks on marker
        therapistMarker.addListener('click', () => {
          therapistInfo.close();
          therapistInfo.setContent(therapistInfoContent);
          therapistInfo.open(map,therapistMarker);
        }); //event listerner marker closed.
        }
        }).fail(() => {
          alert((`
            We could not retrieve data. 
          `));
        }); //close Ajax
        }
   //close initMap
