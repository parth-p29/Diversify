
function bar_graph(data_labels, data, step=10, step_value=0.1, max_value=1.0){
    var ctx = document.getElementById("myChart").getContext('2d');
    new Chart(ctx, {

        // The type of chart we want to create
        type: 'bar',
    
        // The data for our dataset
        data: {
            labels: data_labels,
            
            datasets: [{
                backgroundColor: ['rgb(87, 103, 232, 0.7)', 'rgb(238, 205, 98, 0.7)', 'rgb(98, 238, 112, 0.7)', 'rgb(228, 64, 75, 0.7)', 'rgb(218, 131, 45, 0.7)', 'rgb(151, 56, 235, 0.7)', 'rgb(103, 243, 239, 0.7)'],
                data: data,
                barPercentage: 0.5,
                barThickness: 1,
                maxBarThickness: 1,
                minBarLength: 2,
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
                        steps:step,
                        stepValue: step_value,
                        max: max_value
                    },

                    gridLines: {
                        display: true,
                        color: "rgb(175, 175, 175, 0.3)"
                    }
                }]    
            },
            legend: {
                display: false
            }
        }
    });
}

function radar_graph(user_data, spotify_data){
    var radarChart = document.getElementById('radarChart').getContext('2d');

    new Chart(radarChart, {

        type: 'radar',
        
        data: {
            labels: ['Danceability', 'Energy', 'Acousticness', 'Speechiness', 'Valence', "Instrumentalness"],
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
                label: "Top Spotify Songs in 2020",
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
                    stepSize: 0.1,
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

function doughnut_graph(data1, data2, data3, id){
    var ctx = document.getElementById(id).getContext('2d');

    new Chart(ctx, {
        type: 'doughnut',

        // The data for our dataset
        data: {
            labels: ['Positive', "Negative", "Neutral"],
            datasets: [{
                label: 'Lyrical Sentiment',
                backgroundColor: ['rgb(98, 238, 112, 0.7)', "rgb(228, 64, 75, 0.7)", "rgb(87, 103, 232, 0.7)" ],
                borderColor: ['rgb(98, 238, 112, 0.7)', "rgb(228, 64, 75, 0.7)", "rgb(87, 103, 232, 0.7)" ],
                data: [data1, data2, data3]
            }]
        },

        // Configuration options go here
        options: {}
    });
}