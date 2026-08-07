import React, { useState } from "react";

function App() {
  const [data, setData] = useState(null);

  const predictMarket = () => {
    setData({
      signal: "BUY",
      confidence: "87%",
      sentiment: "Positive",
    });
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Market Predictor</h1>

      <button onClick={predictMarket}>
        Predict Market
      </button>

      {data && (
        <div>
          <h2>Signal: {data.signal}</h2>
          <p>Confidence: {data.confidence}</p>
          <p>Sentiment: {data.sentiment}</p>
        </div>
      )}
    </div>
  );
}

export default App;