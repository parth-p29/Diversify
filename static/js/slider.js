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
var speech_output = document.getElementById("slider-value-Speechiness");
var val_output = document.getElementById("slider-value-Valence");
var instru_output = document.getElementById("slider-value-Instrumentalness");

var button = document.getElementById('button');

pop_output.innerHTML = pop_slider.value;
dance_output.innerHTML = dance_slider.value;
energy_output.innerHTML = dance_slider.value;
acous_output.innerHTML = dance_slider.value;
speech_output.innerHTML = dance_slider.value;
val_output.innerHTML = dance_slider.value;
instru_output.innerHTML = dance_slider.value;

pop_slider.oninput = function() {
    pop_output.innerHTML = this.value;
}

dance_slider.oninput = function() {
    dance_output.innerHTML = this.value;
}

energy_slider.oninput = function() {
    energy_output.innerHTML = this.value;
}

acous_slider.oninput = function() {
    acous_output.innerHTML = this.value;
}

speech_slider.oninput = function() {
    speech_output.innerHTML = this.value;
}

val_slider.oninput = function() {
    val_output.innerHTML = this.value;
}

instru_slider.oninput = function() {
    instru_output.innerHTML = this.value;
}