import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import homepage from "./homepage";


class App extends Component {
    render() {
        return (
            <Router>
                    <div>
                        <Switch>
                            <Route path="/" exact component={homepage}/>
                        </Switch>
                    </div>
                </Router>            
        )
    }
}

ReactDOM.render(<App/>, document.getElementById('app'));