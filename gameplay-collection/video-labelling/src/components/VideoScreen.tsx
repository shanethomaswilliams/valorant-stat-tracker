import React, { useRef} from "react";
import { Player, BigPlayButton } from "video-react";

const VideoScreen: React.FC = () => {
  const url = 'https://www.youtube.com/watch?v=LXb3EKWsInQ'

  return (
    <div className="video-container">
        <Player>
          <source src={url} />
        </Player>
    </div>
  );
};

export default VideoScreen;