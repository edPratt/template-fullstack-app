import React from 'react'
import { ApolloProvider } from 'react-apollo'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router } from 'react-router-dom'

import './styles/bootstrap-theme/template.css'
import './styles/layout.css'

import { client } from './api'
import App from './components/App'
import { unregister } from './registerServiceWorker'

const app = (
    <ApolloProvider client={client}>
        <Router>
            <App />
        </Router>
    </ApolloProvider>
)

ReactDOM.render(app, document.getElementById('root'))
unregister()
