document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('voteChart');
    if (!ctx) return; // Skip if canvas doesn't exist

    const redCount = parseInt(ctx.dataset.red) || 0;
    const amberCount = parseInt(ctx.dataset.amber) || 0;
    const greenCount = parseInt(ctx.dataset.green) || 0;

    new Chart(ctx.getContext('2d'), {
        type: 'bar',
        data: {
            labels: ['Red', 'Amber', 'Green'],
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
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Votes'
                    }
                }
            }
        }
    });
});
