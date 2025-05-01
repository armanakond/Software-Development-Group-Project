//Author: Arman

document.addEventListener('DOMContentLoaded', function () { //this waits till DOM is loaded 
    const ctx = document.getElementById('voteChart');  //the canvas element w ID voteChart
    if (!ctx) return;


    //parseInt used to convert data into integer, so it will be 0 if this is not defined
    const redCount = parseInt(ctx.dataset.red) || 0;
    const amberCount = parseInt(ctx.dataset.amber) || 0;
    const greenCount = parseInt(ctx.dataset.green) || 0;


    new Chart(ctx.getContext('2d'), { //create chart 
        type: 'bar',
        data: {
            labels: ['Red', 'Amber', 'Green'], //the label which is x axis
            datasets: [{
                label: 'Vote Count',
                data: [redCount, amberCount, greenCount],
                backgroundColor: ['#ff4d4d', '#ffcc00', '#33cc33'],
                borderColor: ['#cc0000', '#e6b800', '#248f24'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true, //the numbers which is at y axis.
                    title: {
                        display: true,
                        text: 'Number of Votes'
                    }
                }
            }
        }
    });
});

//https://www.w3schools.com/ai/ai_chartjs.asp
