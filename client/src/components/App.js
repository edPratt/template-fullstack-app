import React, { Component, Fragment } from 'react'
import {
    Route,
    Switch,
} from 'react-router-dom'

import Homepage from './Homepage'
import FinishSteam from './steam/FinishSteam'
import {
    SignupComplete
} from './user'
import {
    About,
    Contact,
    FAQ,
    Rules,
    TwitchStream,
} from './content'
import { Footer, Navigation } from './layout'
import { ContentContainer } from './utils'

class App extends Component {
    render() {
        return (
            <Fragment>
                <Navigation/>
                <section className="flex-grow">
                    <ContentContainer>
                        <Switch>
                            <Route exact path="/" component={Homepage} />
                            <Route exact path="/about" component={About} />
                            <Route exact path="/contact" component={Contact} />
                            <Route exact path="/faqs" component={FAQ} />
                            <Route exact path="/rules" component={Rules} />
                            <Route exact path="/twitch-stream" component={TwitchStream} />
                            <Route path="/signup-complete" component={SignupComplete} />
                            <Route path="/finish-steam/:partial_token" component={FinishSteam} />
                        </Switch>
                    </ContentContainer>
                </section>
                <Footer />
            </Fragment>
        )
    }
}


export default App;
