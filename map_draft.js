"use strict"
function initMap() {
    // Code that works with Google Maps here
    const twinCitiesCoords = {
        lat: 44.9375,
        lng: 93.2010
      };
      
    const basicMap = new google.maps.Map(
        document.querySelector('#map'),
        {
            center: twinCitiesCoords,
            zoom: 11
        }

      );


    // const locations = 
    //python code
    // for t in therapist -- return t.name, t.address, t.latitude, t.longitude. 