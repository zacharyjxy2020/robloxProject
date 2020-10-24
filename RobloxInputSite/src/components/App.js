import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import homepage from "./homepage";
import firebase from 'firebase';

var firebaseConfig = {
    apiKey: "AIzaSyAh25eSpo9KCmkG4GwQYbWMwvj47rpdu58",
    authDomain: "test-project-2e011.firebaseapp.com",
    databaseURL: "https://test-project-2e011.firebaseio.com",
    projectId: "test-project-2e011",
    storageBucket: "test-project-2e011.appspot.com",
    messagingSenderId: "615132454227",
    appId: "1:615132454227:web:c9d5173bed341c212255a6",
    measurementId: "G-NF17JB6TPB"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);



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