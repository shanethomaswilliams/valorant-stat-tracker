import React from "react";
import logo from "./logo.svg";
import "./App.css";
import ImageViewer from "./components/ImageViewer";

function App() {
  // Calculate the relative path to the image data directory
  const currentLocation = window.location.pathname;
  const parentDirectory = currentLocation.substring(
    0,
    currentLocation.lastIndexOf("/")
  );
  const imageDataPath = `${parentDirectory}/../data-creation/data/ability-data`;

  return (
    <div className="App">
      <ImageViewer imageDataPath={imageDataPath} />
    </div>
  );
}

export default App;
