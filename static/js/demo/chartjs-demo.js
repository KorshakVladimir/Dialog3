refrech_radar =  function () {

    var barData = {
        labels: ["Телефоны", "Телевизоры", "Наушники", "Ноутбуки", "Планшеты", "Мониторы", "Фотоапараты"],
        datasets: [
            // {
            //     label: "My First dataset",
            //     fillColor: "rgba(220,220,220,0.5)",
            //     strokeColor: "rgba(220,220,220,0.8)",
            //     highlightFill: "rgba(220,220,220,0.75)",
            //     highlightStroke: "rgba(220,220,220,1)",
            //     data: [65, 59, 80, 81, 56, 55, 40]
            // },
            {
                label: "My Second dataset",
                fillColor: "rgba(26,179,148,0.5)",
                strokeColor: "rgba(26,179,148,0.8)",
                highlightFill: "rgba(26,179,148,0.75)",
                highlightStroke: "rgba(26,179,148,1)",
                data: [28, 48, 40, 19, 86, 27, 90]
            }
        ]
    };

    var barOptions = {
        scaleBeginAtZero: true,
        scaleShowGridLines: true,
        scaleGridLineColor: "rgba(0,0,0,.05)",
        scaleGridLineWidth: 1,
        barShowStroke: true,
        barStrokeWidth: 2,
        barValueSpacing: 5,
        barDatasetSpacing: 1,
        responsive: true,
    }

    try {

    var ctx = document.getElementById("barChart").getContext("2d");
    var myNewChart = new Chart(ctx).Bar(barData, barOptions);
        } catch (err) {

        }


    var radarData = {
        labels: ["Приветствие (Установка контакта)", "Выяснение запросов", "Предложения", "Аргументация", 
        "Работа с возражениями", "Заключение сделки"],
        datasets: [
            {
                label: "My First dataset",
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [65, 59, 90, 81, 80, 50]
            },
            {
                label: "My Second dataset",
                fillColor: "rgba(26,179,148,0.2)",
                strokeColor: "rgba(26,179,148,1)",
                pointColor: "rgba(26,179,148,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(151,187,205,1)",
                data: [28, 48, 40, 19, 46, 27]
            }
        ]
    };
    


    var get_radar_data = function(){
            
            $.getJSON("/report/radar_chart_game").done(function(data){
            // alert( data.something[1]);
            radarData.labels = data["label"];
            // radarData.labels = ["dsdzs","dsdsc"]
            
            radarData.datasets[0].data = data["max_point"];
            // radarData.datasets[0].data = [10,10,40];
            // radarData.datasets[1].data = [40,50,40];
            radarData.datasets[1].data = data["user_point"];
            try {
                var ctx = document.getElementById("radarChart").getContext("2d");
                var myNewChart = new Chart(ctx).Radar(radarData, radarOptions);
                } 
            catch (err) {
            }

        });

 
    };

    var radarOptions = {
        scaleShowLine: true,
        angleShowLineOut: true,
        scaleShowLabels: false,
        scaleBeginAtZero: true,
        angleLineColor: "rgba(0,0,0,.1)",
        angleLineWidth: 1,
        pointLabelFontFamily: "'Arial'",
        pointLabelFontStyle: "normal",
        pointLabelFontSize: 10,
        pointLabelFontColor: "#666",
        pointDot: true,
        pointDotRadius: 3,
        pointDotStrokeWidth: 1,
        pointHitDetectionRadius: 20,
        datasetStroke: true,
        datasetStrokeWidth: 2,
        datasetFill: true,
        responsive: true,
    }

    get_radar_data();
    //-------------------------------------- 
    var barData_all = {
        labels: ["Тел", "ТВ", "Нет", "ibox", "PSP", "IP", "Foto"],
        datasets: [
            // {
            //     label: "My First dataset",
            //     fillColor: "rgba(220,220,220,0.5)",
            //     strokeColor: "rgba(220,220,220,0.8)",
            //     highlightFill: "rgba(220,220,220,0.75)",
            //     highlightStroke: "rgba(220,220,220,1)",
            //     data: [65, 59, 80, 81, 56, 55, 40]
            // },
            {
                label: "My Second dataset",
                fillColor: "rgba(26,179,148,0.5)",
                strokeColor: "rgba(26,179,148,0.8)",
                highlightFill: "rgba(26,179,148,0.75)",
                highlightStroke: "rgba(26,179,148,1)",
                data: [78, 56, 23, 2, 46, 89, 52]
            }
        ]
    };

    var barOptions_all = {
        scaleBeginAtZero: true,
        scaleShowGridLines: true,
        scaleGridLineColor: "rgba(0,0,0,.05)",
        scaleGridLineWidth: 1,
        barShowStroke: true,
        barStrokeWidth: 2,
        barValueSpacing: 5,
        barDatasetSpacing: 1,
        responsive: true,
    }

    try {
    var ctx = document.getElementById("barChart_all").getContext("2d");
    var myNewChart = new Chart(ctx).Bar(barData_all, barOptions_all);
        } catch (err) {

        }

    var radarData_all = {
        labels: ["Приветствие (Установка контакта)", "Выяснение запросов", "Предложения", "Аргументация", 
        "Работа с возражениями", "Заключение сделки"],
        datasets: [
            {
                label: "My First dataset",
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [75, 79, 80, 61, 45, 58]
            },
            {
                label: "My Second dataset",
                fillColor: "rgba(26,179,148,0.2)",
                strokeColor: "rgba(26,179,148,1)",
                pointColor: "rgba(26,179,148,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(151,187,205,1)",
                data: [23, 75, 68, 61, 23, 5]
            }
        ]
    };

    var radarOptions_all = {
        scaleShowLine: true,
        angleShowLineOut: true,
        scaleShowLabels: false,
        scaleBeginAtZero: true,
        angleLineColor: "rgba(0,0,0,.1)",
        angleLineWidth: 1,
        pointLabelFontFamily: "'Arial'",
        pointLabelFontStyle: "normal",
        pointLabelFontSize: 10,
        pointLabelFontColor: "#666",
        pointDot: true,
        pointDotRadius: 3,
        pointDotStrokeWidth: 1,
        pointHitDetectionRadius: 20,
        datasetStroke: true,
        datasetStrokeWidth: 2,
        datasetFill: true,
        responsive: true,
    }
   

    try {
    var ctx = document.getElementById("radarChart_all").getContext("2d");
    var myNewChart = new Chart(ctx).Radar(radarData_all, radarOptions_all);
        } catch (err) {

        }

};