function MessageBubble({ role, content }) {
    return (
        <div
            style={{
                textAlign: role === "user" ? "right" : "left",
                margin: "10px",
            }}
        >
            <span
                style={{
                    padding: "10px",
                    borderRadius: "10px",
                    display: "inline-block",
                    backgroundColor:
                        role === "user" ? "#DCF8C6" : "#F1F0F0",
                }}
            >
                {content}
            </span>
        </div>
    );
}

export default MessageBubble;