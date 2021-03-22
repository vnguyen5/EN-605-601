import * as React from "react";
import { io } from "socket.io-client";
import logo from "./logo.svg";
import "./App.css";
import { WebSocketDemo } from "./components/WebSocketDemo";
import "bootstrap/dist/css/bootstrap.min.css";
import useWebSocket, { ReadyState } from "react-use-websocket";
const socketUrl = "ws://localhost:6789";

function App() {
  const [messages, setMessages] = React.useState([]);

  const {
    sendMessage,
    sendJsonMessage,
    lastMessage,
    lastJsonMessage,
    readyState,
    getWebSocket,
  } = useWebSocket(socketUrl, {
    onOpen: () => console.log("opened"),
    //Will attempt to reconnect on all close events, such as server shutting down
    shouldReconnect: (closeEvent) => true,
    onMessage: (event) => {
      console.log(event.data);
      const tempMessages = messages;
      messages.push(event.data);
      setMessages(tempMessages);
    },
  });

  return <WebSocketDemo messages={messages}/>;
}

export default App;
