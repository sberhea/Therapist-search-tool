"use strict";

const addToBookmark = ("therapist.name") => {
    $('#t-name').append(`
    <li>${"therapist.name"}</li>
    `);
};

$('.bookmark').on('click', () => {
    addToBookmark('therapist.name');
});
