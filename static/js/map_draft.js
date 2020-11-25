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
    const mapOptions = {
      center: { lat: -34.397, lng: 150.644 },
      zoom: 8,
    }
    const map = new google.maps.Map( document.querySelector('#map'),
    mapOptions);
  }

// Retrieve info with AJAX
$.get('api/therapists', (therapists) => {
  for (const therapist of therapists) {
    //Define content of inforWindow
    const therapistInfoContent = (`
    <div class = "window-content">
      <div class = "t-thumbnail">
        <img
          src = therapist.pic">
      </div>
      
      <ul class="therapist-info">
        <li><b>Therapist name: </b>${therapist.name}</li>
      </ul>
    </div>
    `);
  
    const therapistMarker = new google.maps.Marker({
      position: {
        lat: therapist.latitude,
        lng: therapist.longitude
      },
      title: `Therapist ID: ${therapist.therapist_id}`,
      icon: {
        url: therapist.pic,
        scaledSize: new google.maps.Size(50,50)
      },
      map: map,
    });

    therapistMarker.addListener('click', () => {
      therapistInfo.close();
      therapistInfo.setContent(therapistInfoContent);
      therapistInfo.open(map,therapistMarker);
    });
  }
}).fail(() => {
  alert((`
    We could not retrieve data. 
  `));
});
}

    // const locations = 
    //python code
    // for t in therapist -- return t.name, t.address, t.latitude, t.longitude. 