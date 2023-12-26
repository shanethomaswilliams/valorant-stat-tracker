import { useEffect, useState } from 'react';
import './App.css';
import Form from './components/form';
import io from 'socket.io-client';

const socket = io('http://localhost:5000');

function App() {
  const [frames, setFrames] = useState([]);

  useEffect(() => {
    socket.on('connect', () => {
      console.log('Connected to server');
    });

    socket.on('video_info', (data) => {
      console.log('Video info:', data);
    });

    socket.on('frame_pack', (data) => {
      setFrames(data);
    });

    socket.on('video_ended', () => {
      socket.disconnect();
    });
  }, []);

  const handleUrlSubmit = (url: string) => {
    // Handle the submitted URL, e.g., send it to the backend
    console.log('Submitted URL:', url);
    socket.emit('set_video_url', url);
  };
  
  return (
    <div className="App">
      <Form onSubmit={handleUrlSubmit} />
    </div>
  );
}

export default App;
