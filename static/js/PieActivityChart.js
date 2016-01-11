// JavaScript Document
$(function () {
    $('#container').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Activities'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: 'Activities',
            colorByPoint: true,
            data: [{
                name: 'Sleeping',
                y: 50
            }, {
                name: 'Resting',
                y: 20,
                sliced: true,
                selected: true
            }, {
                name: 'Relaxing',
                y: 20
            }, {
                name: 'Snoozing',
                y: 5
            }, {
                name: 'Lolling',
                y: 5
            }]
        }]
    });
});