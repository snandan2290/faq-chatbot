import { useState } from "react";

import ChatInput from "./components/ChatInput";
import ChatWindow from "./components/ChatWindow";

import { sendMessage } from "./services/api";

function App() {
  const [messages, setMessages] = useState([]);

  const sessionId = "session-1";

  const handleSend = async (message) => {
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: message,
      },
    ]);

    try {
      const response = await sendMessage(
        message,
        sessionId
      );

      setMessages((prev) => [
        ...prev,
        {
          role: "bot",
          content: response.answer,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "bot",
          content:
            "Something went wrong.",
        },
      ]);
    }
  };

  return (
    <div>
      <h1>FAQ Chatbot</h1>

      <ChatWindow messages={messages} />

      <ChatInput onSend={handleSend} />
    </div>
  );
}

export default App;