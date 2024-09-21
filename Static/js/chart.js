// document.getElementById('totalSolved').textContent = leetcode_data.totalSolved;
// document.getElementById('acceptanceRate').textContent = leetcode_data.acceptanceRate;
// document.getElementById('ranking').textContent = leetcode_data.ranking.toLocaleString();
// document.getElementById('reputation').textContent = leetcode_data.reputation.toLocaleString();
document.addEventListener("DOMContentLoaded",function () {
    const renderChart1 = (data,labels) =>{
        const ctx = document.getElementById('problemsChart1').getContext('2d');
        var chart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: data,
                    backgroundColor: ['#00b8a3', '#ffc01e', '#ff375f'],
                    borderColor: [
                        "rgba(255, 99, 132, 1)",
                        "rgba(54, 162, 235, 1)",
                        "rgba(255, 206, 86, 1)",
                        "rgba(75, 192, 192, 1)",
                        "rgba(153, 102, 255, 1)",
                        "rgba(255, 159, 64, 1)",
                    ],
                    borderWidth: 1,
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: 'Problems Solved by Difficulty'
                    },
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
    };
    const renderChart2 = (data,labels) =>{
        const ctx = document.getElementById('problemsChart2').getContext('2d');
        var chart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: data,
                    backgroundColor: ['#00b8a3', '#ffc01e', '#ff375f','#ff23f'],
                    borderColor: [
                        "rgba(255, 99, 132, 1)",
                        "rgba(54, 162, 235, 1)",
                        "rgba(255, 206, 86, 1)",
                        "rgba(75, 192, 192, 1)",
                        "rgba(153, 102, 255, 1)",
                        "rgba(255, 159, 64, 1)",
                    ],
                    borderWidth: 1,
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: 'Problems Solved by Difficulty'
                    },
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
    };
    const getChartData = () => {
        console.log("fetching");
        fetch("dashboard/")
          .then((res) => res.json())
          .then((results) => {
            console.log("results", results);
            const leetcode_data = results.leetcode_data;
            const labels1 = ['Easy', 'Medium', 'Hard'];
            const data1 = [leetcode_data.easySolved, leetcode_data.mediumSolved, leetcode_data.hardSolved];
            // console.log(data);
            const github_data = results.github_data;
            const labels2 = ['public_repos', 'public_gists', 'followers','followers'];
            const data2 = [github_data.public_repos, github_data.public_gists, github_data.followers,github_data.followers];
            renderChart1(data1, labels1);
            renderChart2(data2, labels2);

        });
    };
    getChartData();
});

