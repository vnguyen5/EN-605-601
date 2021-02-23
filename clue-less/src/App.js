import * as React from "react";
import { io } from "socket.io-client";
import logo from "./logo.svg";
import "./App.css";

let socket = io('http://localhost:3000')
function App() {
  React.useEffect(() => {
    socket.on("connect", function () {
      socket.emit("echo", { data: "I'm connected!" });
    });
  
  });

 
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          <button onClick={() => socket.em}></button>
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
