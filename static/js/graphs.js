var ctx = document.getElementById('myChart').getContext('2d');

function create_graph(dataa){

    c = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
    
        // The data for our dataset
        data: {
            labels: ['Danceability', 'Energy', 'Acousticness', 'Liveness', 'Speechiness', 'Valence', 'instrumentalness'],
            datasets: [{
                backgroundColor: ['rgb(87, 103, 232, 0.5)', 'rgb(238, 205, 98, 0.5)', 'rgb(98, 238, 112, 0.5)', 'rgb(228, 64, 75, 0.5)', 'rgb(218, 131, 45, 0.5)', 'rgb(151, 56, 235, 0.5)', 'rgb(103, 243, 239, 0.5)'],
                data: dataa,
                scaleOverride:true,
                scaleSteps:0.9,
                scaleStartValue:0,
                scaleStepWidth:0.1
            }]
        },
    
        // Configuration options go here
        options: {
            scales: {
                xAxes: [{
                    gridLines: {
                        display: true,
                        color: "rgb(175, 175, 175, 0.3)"
                    }
                }],
    
                yAxes: [{
                    gridLines: {
                        display: true,
                        color: "rgb(175, 175, 175, 0.3)",
                        opacity: "5%"
                    }
                }
                    ]
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

