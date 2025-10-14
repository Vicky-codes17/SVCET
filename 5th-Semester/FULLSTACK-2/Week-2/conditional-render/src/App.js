import React, { useState } from "react";

export default function App() {
  const [isVisible, setIsVisible] = useState(false);

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      {/* Title */}
      <h1 className="text-2xl font-bold text-gray-800 mb-6">
        Conditional Rendering Example
      </h1>

      {/* Button to toggle component visibility */}
      <button
        onClick={() => setIsVisible(!isVisible)}
        className="px-6 py-2 bg-blue-600 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 transition"
      >
        {isVisible ? "Hide Message" : "Show Message"}
      </button>

      {/* Conditionally rendered component */}
      {isVisible && (
        <div className="mt-8 p-6 bg-white shadow-lg rounded-xl text-center">
          <h2 className="text-xl font-semibold text-green-700">
            Welcome to Professional Conditional Rendering!
          </h2>
          <p className="text-gray-600 mt-3">
            This message is only visible when the button is clicked.
          </p>
        </div>
      )}
    </div>
  );
}







