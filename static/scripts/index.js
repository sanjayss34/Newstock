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
        var url = 'http://localhost:5000/stockdata?symbol='+document.getElementById('symbol').value;
        var xmlhttp = new XMLHttpRequest();
        isLoaded = false;
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                var res = JSON.parse(xmlhttp.responseText);
                dates = res['Dates'];
                prices = res['Prices'];
                symbol = document.getElementById('symbol');
                isLoaded = true;
                if (appObj) {
                    console.log('here');
                    var chart = new Highcharts.Chart({
                        chart: {
                            renderTo: 'chart-container'
                        },
                        xAxis: {
                            categories: dates
                        },
                        series: [{
                            data: prices
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
