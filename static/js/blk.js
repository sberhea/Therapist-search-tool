"use strict";

// $('.add-fav').on('click', (evt) =>{
//     evt.preventDefault();
//     const roaster = $(evt.target);
//     const roaster_id = {roaster: roaster.attr('id')};
//     // console.log(roaster_id);
//     $.get('/add_to_fav_list', roaster_id, (res) => {
//         alert(res);
//     });
    
// })

// const addToBookmark = ("therapist.name") => {
//     $('#t-name').append(`
//     <li>${"therapist.name"}</li>
//     `);
// addToBookmark('therapist.name');
// };

$('.add-bookmark').on('click', (evt) => {
    evt.preventDefault
    const therapist = $(evt.target);
    const therapist_id = {therapist: therapist.attr('id')};
    $.get('/bookmark', therapist_id, (res) => {
        alert(res);
    });
})

$(document).ready(function(){
    $('.header').height($(window).height());
  })
