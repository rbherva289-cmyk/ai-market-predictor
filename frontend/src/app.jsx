import React, { useState } from "react";

function App() {
  const [prediction, setPrediction] = useState(null);

  const getPrediction = async () => {
    setPrediction({
      symbol: "NIFTY",
      signal: "BUY",
      confidence: "87%",
    });
  };

  return (
    <div style={{ padding: "20px", textAlign: "center" }}>
      <h1>AI Market Predictor</h1>

      <button onClick={getPrediction}>
        Predict Market
      </button>

      {prediction && (
        <div>
          <h2>{prediction.symbol}</h2>
          <p>Signal: {prediction.signal}</p>
          <p>Confidence: {prediction.confidence}</p>
        </div>
      )}
    </div>
  );
}

export default App;