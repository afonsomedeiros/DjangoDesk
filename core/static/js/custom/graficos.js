function por_sistema(){

}

$(document).ready(function () {
    /* Voltar ao topo */
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });

    $('#back-to-top').click(function () {
        
        return false;
    });

    /* primeiro gráfico do dash */
    var ctx = document.getElementById('myChart').getContext('2d');
    $.get("/dashboard/grafico1/", function(data){
        var l = [];
        var num = [];
        for (var i = 0; i < data.length; i++) {
            l.push(data[i]['empresa__sistema__nome'])
            num.push(data[i]['total'])
        }
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: l,
                datasets: [{
                    label: 'Registros do sistema',
                    data: num,
                    backgroundColor: [
                        'rgba(0, 0, 160, .3)',
                        'rgba(0, 0, 160, .3)',
                        'rgba(0, 0, 160, .3)',
                        'rgba(0, 0, 160, .3)',
                        'rgba(0, 0, 160, .3)'
                    ]
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    })

    /* segundo gráfico */
    var ctx2 = document.getElementById('myChart2').getContext('2d');
    $.get("/dashboard/grafico2", function(data){
        var l = [];
        var num = [];
        for (var i = 0; i < data.length; i++) {
            l.push(data[i]['empresa__nome_fantasia'])
            num.push(data[i]['total'])
        }
        var myChart2 = new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: l,
                datasets: [{
                    label: '5 Clientes que mais ligaram na semana',
                    data: num,
                    backgroundColor: [
                        'rgba(160, 0, 0, .3)',
                        'rgba(160, 0, 0, .3)',
                        'rgba(160, 0, 0, .3)',
                        'rgba(160, 0, 0, .3)'
                    ]
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    });

    /* terceiro gráfico */
    var ctx3 = document.getElementById('myChart3').getContext('2d');
    $.get("/dashboard/grafico3/", function(data){
        var l = [];
        var num = [];
        var dias_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
        for (var i = 0; i < data.length; i++) {
            data[i]['weekday'] = dias_semana[data[i]['weekday']-1]
        }
        for (var i = 0; i < data.length; i++) {
            l.push(data[i]['weekday'])
            num.push(data[i]['count'])
        }
        var myChart3 = new Chart(ctx3, {
            type: 'bar',
            data: {
                labels: l,
                datasets: [{
                    label: 'Registros do sistema',
                    data: num,
                    backgroundColor: [
                        'rgba(0, 160, 0, .3)',
                        'rgba(0, 160, 0, .3)',
                        'rgba(0, 160, 0, .3)',
                        'rgba(0, 160, 0, .3)',
                        'rgba(0, 160, 0, .3)',
                        'rgba(0, 160, 0, .3)',
                        'rgba(0, 160, 0, .3)'
                    ]
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    });
});