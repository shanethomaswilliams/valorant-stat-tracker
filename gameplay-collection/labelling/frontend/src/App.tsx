import { useEffect, useState } from 'react';
import './App.css';
import Form from './components/form';
import { io } from "socket.io-client";

function App() {
  const [socketInstance, setSocketInstance] = useState(io);
  const [loading, setLoading] = useState(false);
  const [buttonStatus, setButtonStatus] = useState(false);

  useEffect(() => {
    const socket = io("localhost:5001/", {
      transports: ["websocket"],
    });
  
    socket.on("/connect", (data: any) => {
      setSocketInstance(socket);
      setLoading(true);
      console.log("socket connected: ", data);
    });

    socket.on("/error", (error: any) => {
      // TODO: Complete clearing input field and display error message
      console.log("received error message: \n", error["message"]);
    });

    socket.on("/video_info", (info: any) => {
      console.log(info);
    })

    socket.on("/frame", (frame: any) => {
      if (loading) {
        setLoading(false);
      }
      console.log("Received two seconds of frames!");
    });

    socket.on("/video_ended", (end_message: any) => {
      console.log(end_message);
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