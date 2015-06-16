/*jshint quotmark:false */
/*jshint white:false */
/*jshint trailing:false */
/*jshint newcap:false */
/*global React, Router*/
var app = app || {};

(function () {
	'use strict';

	app.ALL_BOARDS = 'all';
	app.ACTIVE_BOARDS = 'active';
	app.COMPLETED_BOARDSS = 'completed';
	var TodoFooter = app.TodoFooter;
	var Board = app.Board;

	var ENTER_KEY = 13;

	var TodoApp = React.createClass({
		getInitialState: function () {
			return {
				nowShowing: app.ALL_BOARDS,
				editing: null
			};
		},

		componentDidMount: function () {
			var setState = this.setState;
			var router = Router({
				'/': setState.bind(this, {nowShowing: app.ALL_BOARDS}),
				'/active': setState.bind(this, {nowShowing: app.ACTIVE_BOARDS}),
				'/completed': setState.bind(this, {nowShowing: app.COMPLETED_BOARDS})
			});
			router.init('/');
		},

		handleNewTodoKeyDown: function (event) {
			if (event.which !== ENTER_KEY) {
					return;
			}

			event.preventDefault();

			var val = this.refs.newField.getDOMNode().value.trim();

			if (val) {
				this.props.model.addBoard(val);
				this.refs.newField.getDOMNode().value = '';
			}
		},

		toggleAll: function (event) {
			var checked = event.target.checked;
			this.props.model.toggleAll(checked);
		},

		toggle: function (boardToToggle) {
			this.props.model.toggle(boardToToggle);
		},

		destroy: function (board) {
			this.props.model.destroy(board);
		},

		edit: function (board) {
			this.setState({editing: board.id});
		},

		save: function (boardToSave, text) {
			this.props.model.save(boardToSave, text);
			this.setState({editing: null});
		},

		cancel: function () {
			this.setState({editing: null});
		},

		clearCompleted: function () {
			this.props.model.clearCompleted();
		},

		render: function () {
			var footer;
			var main;
			var boards = this.props.model.boards;

			var shownBoards = boards.filter(function (boards) {
				switch (this.state.nowShowing) {
				case app.ACTIVE_TODOS:
					return !todo.completed;
				case app.COMPLETED_TODOS:
					return todo.completed;
				default:
					return true;
				}
			}, this);

			var boards = shownTodos.map(function (board) {
				return (
					<Board
						key={board.id}
						board={board}
						onToggle={this.toggle.bind(this, board)}
						onDestroy={this.destroy.bind(this, board)}
						onEdit={this.edit.bind(this, board)}
						editing={this.state.editing === board.id}
						onSave={this.save.bind(this, board)}
						onCancel={this.cancel}
					/>
				);
			}, this);

			var activeBoardCount = boards.reduce(function (accum, board) {
				return board.completed ? accum : accum + 1;
			}, 0);

			var completedCount = board.length - activeTodoCount;

			if (activeBoardCount || completedCount) {
				footer =
					<TodoFooter
						count={activeTodoCount}
						completedCount={completedCount}
						nowShowing={this.state.nowShowing}
						onClearCompleted={this.clearCompleted}
					/>;
			}

			if (todos.length) {
				main = (
					<section id="main">
						<input
							id="toggle-all"
							type="checkbox"
							onChange={this.toggleAll}
							checked={activeTodoCount === 0}
						/>
						<ul id="board-list">
							{BoardItems}
						</ul>
					</section>
				);
			}

			return (
				<div>
					<header id="header">
						<h1>todos</h1>
						<input
							ref="newField"
							id="new-todo"
							placeholder="What needs to be done?"
							onKeyDown={this.handleNewTodoKeyDown}
							autoFocus={true}
						/>
					</header>
					{main}
					{footer}
				</div>
			);
		}
	});

	var model = new app.BoardModel('react-boards');

	function render() {
		React.render(
			<TodoApp model={model}/>,
			document.getElementById('todoapp')
		);
	}

	model.subscribe(render);
	render();
})();
