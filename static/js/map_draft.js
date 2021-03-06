"use strict"
let map;

function initMap() {
  
  const map = new google.maps.Map( document.querySelector('#map'),{
    center: { lat: 44.9778, lng: -93.2650 },
    zoom: 11,
  }); //close base map

const therapistInfo = new google.maps.InfoWindow();


    // Retrieve info with AJAX
    const jsonURL = "/api/therapists";

    $.get(jsonURL, (therapists) => {
    
      for (let therapist of therapists) {
        //Define content of infoWindow
        const therapistInfoContent = (`
        <div class = "window-content">
          
          <ul class="therapist-info">
            <li><div class = "t-thumbnail">
            <img src = ${therapist.pic}>
            </div></li>
            <br>
            <li><b>Name: </b>${therapist.name}</li>
            <li><b>Description: </b>${therapist.description}</li>
            <li><b>Call: </b>${therapist.phonenum}</li>
            <li><a href = ${therapist.fp}> Link to full profile </a></li>
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
          // icon: {
          //   url: therapist.pic,
          //   scaledSize: new google.maps.Size(50,50)
          // },
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
