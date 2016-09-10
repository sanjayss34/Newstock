var isLoaded = false;
var symbol = "";
var prices = null;
var dates = null;
var appObj = null;

var NavBar = React.createClass({
    render: function() {
        return React.createElement('nav', {className: "navbar navbar-default"},
            React.createElement('div', {className: 'container-fluid'},
                React.createElement('div', {className: 'navbar-header'},
                    React.createElement('a', {className: 'navbar-brand', href: "#"}, "Newstock"))));
    }
});

var InputForm = React.createClass({
    submitForm: function(e) {
        e.preventDefault();
        /*ReactDOM.render(React.createElement('div', {className: 'progress', style: {width: '100%'}},
            React.createElement('div', {className: 'progress-bar progress-bar-striped active', role: 'progressbar'})), document.getElementById('chart-container'));*/
        ReactDOM.render(React.createElement('div', {style: {width: "30%", textAlign: "center"}}, React.createElement('ProgressBar', {className: 'active', now: "100%"})), document.getElementById('chart-container'));
        var url = 'http://localhost:5000/stockdata?symbol='+document.getElementById('symbol').value;
        var xmlhttp = new XMLHttpRequest();
        isLoaded = false;
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                var res = JSON.parse(xmlhttp.responseText);
                dates = res['Dates'];
                prices = res['Prices'];
                symbol = document.getElementById('symbol').value.toUpperCase();
                isLoaded = true;
                var polarities = [];
                console.log(res['ArticleData']);
                for(i = 0; i < dates.length; i++) {
                    if (dates[i] in res['ArticleData']) {
                        var meanVal = 0.0
                        for (j = 0; j < res['ArticleData'][dates[i]].length; j++) {
                            meanVal = meanVal + res['ArticleData'][dates[i]][j][1];
                        }
                        meanVal = meanVal/res['ArticleData'][dates[i]].length;
                        console.log(meanVal);
                        polarities.push(meanVal);
                    }
                    else {
                        polarities.push(0.0);
                    }
                }
                console.log(polarities)
                if (appObj) {
                    var chart = new Highcharts.Chart({
                        chart: {
                            renderTo: 'chart-container',
                            zoomType: 'xy',
                            backgroundColor:'rgba(255, 255, 255, 0.7)'
                        },
                        title: {
                            text: symbol + ': Last 30 Days'
                        },
                        xAxis: {
                            categories: dates
                        },
                        yAxis: [{
                            title: {
                                text: 'Stock Price'
                            },
                            labels: {
                                format: '${value}'
                            },
                            opposite: false
                        }, {
                            title: {
                                text: 'Rating'
                            },
                            min: -1.0,
                            max: 1.0,
                            opposite: true
                        }],
                        series: [{
                            name: 'Price',
                            type: 'spline',
                            yAxis: 0,
                            data: prices
                        }, {
                            name: 'Rating',
                            type: 'spline',
                            yAxis: 1,
                            data: polarities
                        }]
                    });
                }
            }
        };
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
    },

    render: function() {
        return React.createElement('form', {className: 'form-inline', onSubmit: this.submitForm},
            React.createElement('div',
                {className: "input-group",
                 style: {width: "100%", textAlign: 'center'}
                },
                React.createElement('div',
                {className: 'col-xs-15',
                 style: {display: 'inline-block'}
                },
                React.createElement("input",
                {type: "text",
                className: "form-control",
                id: "symbol",
                style: {borderRadius: "10px 0px 0px 10px"}
                }),
                React.createElement("button",
                {type: "submit",
                 className: "btn btn-default",
                 style: {borderRadius: "0px 10px 10px 0px"}
                }, 'Submit'))));
    }
});

var App = React.createClass({
    displayName: 'App',

    render: function() {
        return React.createElement('div', {},
            React.createElement(NavBar),
            React.createElement(InputForm));
    }
});

appObj = React.createElement(App)

ReactDOM.render(appObj, document.getElementById('body'));
