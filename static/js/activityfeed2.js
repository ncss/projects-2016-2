$(function () {
    $('#activity_feed2').highcharts({
        title: {
            text: '',
            x: -20 //center
        },
        subtitle: {
            text: '',
            x: -20
        },
        xAxis: {
            categories: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
                'Sunday']
        },
        yAxis: {
            title: {
                text: 'Time (mins)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: ' minutes'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: 'Tennis',
            data: [50,49,35,45,55,55,33]
        },{
        		name: 'Swimming',
            data:[45,15,17,15,16,36,53]
        },{
        		name: 'Cycling',
            data:[103,81,33,14,0,48,79]
        }      
        ]
    });
});