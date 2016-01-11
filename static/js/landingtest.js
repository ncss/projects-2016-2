$(function () {
	$('#linecontainer').highcharts({
        title: {
            text: "Weekly Activities",
            x: -20 //center
        },
        xAxis: {
            categories: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        },
        yAxis: {
            title: {
                text: "Distance (km)"
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: "#808080"
            }]
        },
        tooltip: {
            valueSuffix: "km"
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: "Swimming",
            data: [1, 3, 2, 2.5, 0, 7, 0],
			color: "#deff00"
        }, {
            name: "Walking",
            data: [10, 16, 0, 7, 3, 5, 4],
			color: "#ff4200"
        }, {
            name: "Cycling",
            data: [0, 0, 10, 5, 5, 4, 7],
			color: "#00d2ff"
        }]
    });
});