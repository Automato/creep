import React from 'react'
import ReactDOM from 'react-dom'
import createBrowserHistory from 'history/lib/createBrowserHistory'
import { useRouterHistory } from 'react-router'
import { syncHistoryWithStore } from 'react-router-redux'
import createStore from './store/createStore';
import AppContainer from './containers/AppContainer';


// Setup browser history
const browserHistory = useRouterHistory(createBrowserHistory)(
  {
    basename: __BASENAME__
  }
)

// Create redux store and sync with react-router-redux
const initialState = window.__INITIAL_STATE__
const store = createStore(initialState, browserHistory);
const history = syncHistoryWithStore(
  browserHistory,
  store,
  {
    selectLocationState: (state) => state.router
  }
)

// Enable developer tools
if (__DEBUG__) {
  if (window.devToolsExtension) {
    window.devToolsExtension.open()
  }
}

// Setup render function normally
const MOUNT_NODE = document.getElementById('root')

let render = (routerKey=null) => {
  const routes = require('./routes/index').default(store)

  ReactDOM.render(
    <AppContainer
      store={store}
      history={history}
      routes={routes}
      routerKey={routerKey}
    />,
    MOUNT_NODE
  )
}

// Enable Hot Module Reload and catch runtime errors in
// React RedBox; This code is excluded from production bundle
if (__DEV__ && module.hot) {
  const renderApp = render
  const renderError = (error) => {
    const RedBox = require('redbox-react')

    ReactDom.render(
      <RedBox
        error={error}
      />,
      MOUNT_NODE
    )

    render = () => {
      try {
        renderApp(Math.random())
      } catch (error) {
        renderError(error)
      }
    }
    module.hot.accept(['./routes/index'], () => render())
  }
}

render()
