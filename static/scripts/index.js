var InitialComponent = React.createClass({
    render: function() {
        return React.createElement('div', {}, 'Hello, world');
    }
});

ReactDOM.render(React.createElement(InitialComponent), document.getElementById('body'));
