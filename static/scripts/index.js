var NavBar = React.createClass({
    render: function() {
        return React.createElement('nav', {className: "navbar navbar-default"},
            React.createElement('div', {className: 'container-fluid'},
                React.createElement('div', {className: 'navbar-header'},
                    React.createElement('a', {className: 'navbar-brand', href: "#"}, "Newstock"))));
    }
});

var InputForm = React.createClass({
    render: function() {
        return React.createElement('form', {className: 'form-inline'},
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
    render: function() {
        return React.createElement('div', {},
            React.createElement(NavBar),
            React.createElement(InputForm));
    }
});

ReactDOM.render(React.createElement(App), document.getElementById('body'));
