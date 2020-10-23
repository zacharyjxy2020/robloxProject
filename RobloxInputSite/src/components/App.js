import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import { Route } from 'react-router';


class App extends Component {
    render() {
        return (
            <Router>
                    <div>
                        <Switch>
                            <Route path="/homepage" exact component={homepage}/>
                        </Switch>
                    </div>
                </Router>            
        )
    }
}

ReactDOM.render(<App/>, document.getElementById('app'));