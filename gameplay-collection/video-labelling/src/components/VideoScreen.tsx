import React, { useRef, useState } from "react";
import { Player, BigPlayButton } from "video-react";
import ReactPlayer from 'react-player'

const VideoSeekComponent: React.FC = () => {
  const videoRef = useRef<HTMLVideoElement>();
  const [videoUrl, setVideoUrl] = useState("https://example.com/video.mp4");
  const [seekTime, setSeekTime] = useState(10);

  const url = 'https://www.youtube.com/watch?v=LXb3EKWsInQ'

  return (
    <div className="video-container">
        <Player>
          <source src="https://media.w3.org/2010/05/sintel/trailer_hd.mp4" />
        </Player>
    </div>
  );
};

export default VideoSeekComponent;