import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const sendMessage = async (message, sessionId) => {
  const response = await api.post("/chat", {
    session_id: sessionId,
    message,
  });

  return response.data;
};
