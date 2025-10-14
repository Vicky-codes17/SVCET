import React, { useState } from "react";

function ButtonEvents() {
  const [message, setMessage] = useState("Click any button to see action!");

  const handleGreet = () => {
    setMessage("Hello! You clicked the Greet button ");
  };

  const handleBye = () => {
    setMessage("Goodbye! You clicked the Bye button ");
  };

  const handleReset = () => {
    setMessage("Click any button to see action!");
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>React Button Click Event Handling</h2>

      {/* Display message */}
      <p>{message}</p>

      {/* Buttons with their respective click handlers */}
      <button onClick={handleGreet} style={{ margin: "5px" }}>
        Greet
      </button>

      <button onClick={handleBye} style={{ margin: "5px" }}>
        Bye
      </button>

      <button onClick={handleReset} style={{ margin: "5px" }}>
        Reset
      </button>
    </div>
  );
}
// Export the component
export default ButtonEvents;