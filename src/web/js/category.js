var app = app || {};

(function () {
  'use strict';

  var Category = React.createClass({
    render: function() {
      return "Category";
    }
  });

  var CategoryModel = function() {
    this.key = key;
    this.todos = Utils.store(key);
    this.onChanges = [];
  };

  app.CategoryModel.prototype.subscribe = function (onChange) {
    this.onChanges.push(onChange);
  };

  app.CategoryModel.prototype.inform = function () {
    Utils.store(this.key, this.todos);
    this.onChanges.forEach(function (cb) { cb(); });
  };

  app.CategoryModel.prototype.addCategory = function (title) {
    this.todos = this.todos.concat({
      id: Utils.uuid(),
      title: title
    });

    this.inform();
  };

  app.CategoryModel.prototype.destroy = function (todo) {
    this.todos = this.todos.filter(function (candidate) {
      return candidate !== todo;
    });

    this.inform();
  };

  app.CategoryModel.prototype.save = function (todoToSave, text) {
    this.todos = this.todos.map(function (todo) {
      return todo !== todoToSave ? todo : Utils.extend({}, todo, {title: text});
    });

    this.inform();
  };

})();