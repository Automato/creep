var app = app || {};

(function () {
  'use strict'

  var CardBoardApp = React.createClass({
    displayName: "CardBoardApp",
    getInitialState: function () {
      return {

      };
    },
    render: function () {
      return React.DOM.div(null, 'Hello World!');
    }
  });

  var model = new app.BoardModel('');

  function render() {
    var BoardFactory = React.createFactory(CardBoardApp);
    var board = BoardFactory({model: model});
    React.render(board, document.getElementById('cardboardapp'));
  }
  model.subscribe(render);
  render();
})();