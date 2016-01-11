// <div id="activity_feed3" style="min-width: 310px; height: 400px; margin: 0 auto"></div>
$(function () {
    $('#activity_feed3').highcharts({
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
            name: 'Running',
            data: [50,49,35,45,55,55,33]
        },{
        		name: 'Skipping',
            data:[15,98,28,23,59,30,40]
        },{
        		name: 'Quidditch',
            data:[60,30,10,40,0,30,79]
        }      
        ]
    });
});