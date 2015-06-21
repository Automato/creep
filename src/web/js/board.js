var app = app || {};

(function () {
  'use strict';

  var Board = React.createClass({
    render: function() {
      return "Board";
    }
  });

  var BoardModel = Backbone.Model.extend({
      defaults : {
        'title': ''
      }
  });

})();