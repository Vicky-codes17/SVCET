// Import React and the useState Hook
import React, { useState } from "react";

// Define a Functional Component named Counter
function Counter() {
  // Declare a state variable 'count' and its setter 'setCount'
  // useState(0) initializes count with value 0
  const [count, setCount] = useState(0);

  // Function to handle button click and update state
  const increment = () => {
    setCount(count + 1);
  };

  // Return JSX (UI) to render
  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      {/* Heading of the application */}
      <h2>React Counter Application (Functional Component)</h2>

      {/* Display the current counter value */}
      <p>Current Count: {count}</p>

      {/* Button to increase the counter value */}
      <button onClick={increment}>Increase Counter</button>
    </div>
  );
}

// Export the component so it can be used in App.js
export default Counter;
