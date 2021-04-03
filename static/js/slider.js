var pop_slider = document.getElementById("pop");
var dance_slider = document.getElementById("Danceability");
var energy_slider = document.getElementById("Energy");
var acous_slider = document.getElementById("Acousticness");
var speech_slider = document.getElementById("Speechiness");
var val_slider = document.getElementById("Valence");
var instru_slider = document.getElementById("Instrumentalness");

var pop_output = document.getElementById("value");

var dance_output = document.getElementById("slider-value-Danceability");
var energy_output = document.getElementById("slider-value-Energy");
var acous_output = document.getElementById("slider-value-Acousticness");

pop_output.innerHTML = pop_slider.value;
dance_output.innerHTML = dance_slider.value;

pop_slider.oninput = function() {
    pop_output.innerHTML = this.value;
}

dance_slider.oninput = function() {
    dance_output.innerHTML = this.value;
}
