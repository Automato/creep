var app = app || {};

(function () {
  'use strict';

  var Utils = app.Utils;

  app.BoardModel = function (key) {
    this.key = key;
    this.boards = Utils.store(key);
    this.onChanges = [];
  };

  app.BoardModel.prototype.subscribe = function (onChange) {
    this.onChanges.push(onChange);
  };

  app.BoardModel.prototype.inform = function () {
    Utils.store(this.key, this.boards);
    this.onChanges.forEach(function (cb) { cb(); });
  };

  app.BoardModel.prototype.addBoard = function (title) {
    this.boards = this.boards.concat({
      id: Utils.uuid(),
      title: title
    });

    this.inform();
  };

  app.BoardModel.prototype.destroy = function (board) {
    this.boards = this.boards.filter(function (candidate) {
      return candidate !== board;
    });

    this.inform();
  };

  app.BoardModel.prototype.save = function (boardToSave, text) {
    this.boards = this.boards.map(function (board) {
      return board !== boardToSave ? board : Utils.extend({}, board, {title: text});
    });

    this.inform();
  };
})();