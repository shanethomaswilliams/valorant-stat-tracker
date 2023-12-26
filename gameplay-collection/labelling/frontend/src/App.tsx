import { useEffect, useState } from 'react';
import './App.css';
import Form from './components/form';
import { io } from "socket.io-client";



function App() {
  const [socketInstance, setSocketInstance] = useState(io);
  const [loading, setLoading] = useState(true);
  const [buttonStatus, setButtonStatus] = useState(false);

  useEffect(() => {
    const socket = io("localhost:5001/", {
      transports: ["websocket"],
    });
  
    socket.on("/connect", (data: any) => {
      setSocketInstance(socket);
      console.log("socket connected: ", data);
    });

    socket.on("/error", (error: any) => {
      console.log("received error message: \n", error["message"]);
    });

    socket.on("frame", (frame) => {
      console.log(frame)
    });

    socket.on("/video_ended", (data) => {
      console.log(data)
    });

    return () => {
      socket.disconnect();
    }
  }, []);

  const handleUrlSubmit = (url: string) => {
    // Handle the submitted URL, e.g., send it to the backend
    console.log('submitted URL: ', url);
    if (socketInstance) {
      socketInstance.emit("video_url", url);
    }
  };
  
  return (
    <div className="App">
      <Form onSubmit={handleUrlSubmit} />
    </div>
  );
}

export default App;