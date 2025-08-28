// Import React and Component class from react library
import React, { Component } from "react";

// Define a class component named Counter
class Counter extends Component {
  // The constructor is used to initialize the component
  constructor(props) {
    super(props);

    // Initialize the state object with a property 'count'
    // Here, count is set to 0 initially
    this.state = {
      count: 0
    };
  }

  // Define a function to increment the count value
  // setState() is the React method used to update state
  // When state changes, the component automatically re-renders
  increment = () => {
    this.setState({ count: this.state.count + 1 });
  };

  // The render() method returns the JSX (UI) for this component
  render() {
    return (
      <div style={{ textAlign: "center", marginTop: "50px" }}>
        {/* Heading of the application */}
        <h2>React Counter Application</h2>

        {/* Display the current value of 'count' from state */}
        <p>Current Count: {this.state.count}</p>

        {/* Button that triggers increment() function on click */}
        <button onClick={this.increment}>Increase Counter</button>
      </div>
    );
  }
}

// Export the Counter component so it can be imported in App.js
export default Counter;
