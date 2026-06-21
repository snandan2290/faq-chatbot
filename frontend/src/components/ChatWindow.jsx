import MessageBubble from "./MessageBubble";

function ChatWindow({ messages }) {
    return (
        <div>
            {messages.map((msg, index) => (
                <MessageBubble
                    key={index}
                    role={msg.role}
                    content={msg.content}
                />
            ))}
        </div>
    );
}

export default ChatWindow;