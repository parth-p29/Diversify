
function bar_graph(data_labels, audio_data){
    var ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
    
        // The data for our dataset
        data: {
            labels: data_labels,
            datasets: [{
                backgroundColor: ['rgb(87, 103, 232, 0.7)', 'rgb(238, 205, 98, 0.7)', 'rgb(98, 238, 112, 0.7)', 'rgb(228, 64, 75, 0.7)', 'rgb(218, 131, 45, 0.7)', 'rgb(151, 56, 235, 0.7)', 'rgb(103, 243, 239, 0.7)'],
                data: audio_data
    
            }]
        },
    
        // Configuration options go here
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    gridLines: {
                        display: true,
                        color: "rgb(175, 175, 175, 0.3)"
                    }
                }],
    
                yAxes: [{
                    display:true,
                    
                    ticks: {
                        beginAtZero: true,
                        steps:10,
                        stepValue: 0.1,
                        max: 1.0
                    },

                    gridLines: {
                        display: true,
                        color: "rgb(175, 175, 175, 0.3)",
                        opacity: "5%"
                    }
                }]
                    
            },
            legend: {
                display: false
            },
            tooltips: {
                callbacks: {
                label: function(tooltipItem) {
                        return tooltipItem.yLabel;
                }
                }
            }
        }
    });

}


function radar_graph(user_data, spotify_data){
    var radarChart = document.getElementById('radarChart').getContext('2d');

    new Chart(radarChart, {

        type: 'radar',
        
        data: {
            labels: ['Danceability', 'Energy', 'Acousticness', 'Speechiness', 'Positivity', "Instrumentalness"],
            datasets: [{
                data: user_data,
                backgroundColor: ['rgba(233, 72, 96, 0.5)'],
                borderColor: ['rgba(229, 25, 56, 0.97)'],
                borderWidth: 2,
                label: "You",
                pointBackgroundColor: "rgba(169, 4, 23, 0.63)"
            }, 
            
            {

                data: spotify_data,
                backgroundColor: ['rgba(47, 124, 33, 0.5)'],
                borderColor: ['rgba(47, 124, 33, 0.97)'],
                borderWidth: 2,
                label: "Top Spotify Songs",
                pointBackgroundColor: "rgba(26, 169, 4, 0.63)"
            }]
        },
        
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scale: {
                pointLabels: {
                    fontSize: 15
                },

                angleLines: {
                    display: true,
                    color: "rgba(255, 255, 255, 0.74)"
                },

                gridLines :{
                    display: true,
                    color: "rgb(175, 175, 175, 0.3)",
                    opacity: "5%"
                },

                ticks: {
                    beginAtZero: true,
                    stepValue: 2,
                    max: 1.0,
                    backdropColor: "#181818"
                }
            },

            legend: {
                display: true,   
            },

            tooltips: {
                enabled: true,
                callbacks: {
                    label: function(tooltipItem, data) {
                        return data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
                    }
                }
            }

        }

    });

}


function doughnut_graph(data1, data2, id){
    var ctx = document.getElementById(id).getContext('2d');

    new Chart(ctx, {
        type: 'doughnut',

        // The data for our dataset
        data: {
            labels: ['You'],
            datasets: [{
                label: 'Popularity of your top Songs',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [0, 10, 5, 2, 20, 30, 45]
            }]
        },

        // Configuration options go here
        options: {}
});

}