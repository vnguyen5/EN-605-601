import * as React from "react";
import { Clueless, MessageInterface } from "./ClueLess";
import "bootstrap/dist/css/bootstrap.min.css";
import useWebSocket, { ReadyState } from "react-use-websocket";
const socketUrl = "ws://localhost:6789";

export const ClueLessWrapper = () => {
  const [messages, setMessages] = React.useState<MessageInterface[]>([]);

  const onMessageReceived = (event: MessageEvent) => {
    const tempMessages = messages;
    tempMessages.push(JSON.parse(event.data));
    console.log(tempMessages);
    setMessages(tempMessages);
  };

  const {
    sendMessage,
    sendJsonMessage,
    lastMessage,
    lastJsonMessage,
    readyState,
    getWebSocket,
  } = useWebSocket(socketUrl, {
    onOpen: (event) => console.log("opened", event),
    //Will attempt to reconnect on all close events, such as server shutting down
    shouldReconnect: (closeEvent) => true,
    onMessage: onMessageReceived,
  });

  const sendMessageWrapper = React.useCallback((message: MessageInterface) => {
    sendMessage(JSON.stringify(message));
  }, []);

  const sendOnStartMessage = () => {
    const startMessage: MessageInterface = {
      message: "Game Started",
      type: "state",
      action: "start",
    };
    sendMessageWrapper(startMessage);
  };

  const sendOnMoveMessage = () => {
    const moveMessage: MessageInterface = {
      message: "Player Moved",
      type: "state",
      action: "move",
    };

    sendMessageWrapper(moveMessage);
  };

  const sendOnMakeSuggestionMessage = () => {
    const suggestionMessage: MessageInterface = {
      message: "Player Made Suggestion",
      type: "state",
      action: "suggest",
    };
    sendMessageWrapper(suggestionMessage);
  };

  const sendOnAccuseMessage = () => {
    const accuseMessage: MessageInterface = {
      message: "Player Made Accusation",
      type: "state",
      action: "accuse",
    };

    sendMessageWrapper(accuseMessage);
  };

  const sendOnQuitMessage = () => {
    const quitMessage: MessageInterface = {
      message: "Player Quits",
      type: "user",
      action: "quits",
    };
    sendMessageWrapper(quitMessage);
    window.close();
  };
  return (
    <Clueless
      messages={messages}
      onStart={sendOnStartMessage}
      onMove={sendOnMoveMessage}
      onMakeSuggestion={sendOnMakeSuggestionMessage}
      onAccuse={sendOnAccuseMessage}
      onQuit={sendOnQuitMessage}
    />
  );
};
