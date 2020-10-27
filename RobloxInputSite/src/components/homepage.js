import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import firebase, { initializeApp } from 'firebase';
import credentials from 'firebase';
import firestore from 'firebase';

class homepage extends Component {
    render(){
        return(
            <div>
                <form>
                    <label>ENTER YOUR MESSAGE</label>
                    <input type="text" id="textInput"></input>
                    <button type="submit" onClick={submitData} id="submitButton">submit</button>
                </form>
            </div>
        );
    }
}
const submitData = () => {
    console.log('HELLLOOOOOOOOOOOO')
    const db = firebase.firestore()
    const db_ref = db.collection('Data').doc('messages')
    const message = document.getElementById('textInput').value
    document.write('success')
    db_ref.set({
        'message' : message
    })
}

export default homepage