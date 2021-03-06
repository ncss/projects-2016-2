$(function () {
    $('#container').highcharts({
        title: {
            text: 'Weekly',
            x: -20 //center
        },
		
        xAxis: {
            categories: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
                'Sunday']
        },
        yAxis: {
            title: {
                text: 'Distance (km)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: 'km'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: '{{}}',
            data: ["{{'", "'.join(<database thingy>)}}"]
        }, {
            name: '{{}}',
            data: ["{{'", "'.join(<database thingy>)}}"]
        }, {
            name: '{{}}',
            data: ["{{'", "'.join(<database thingy>)}}"]
        }]
    });
});