import React, { useEffect, useRef, useState } from "react";
import { motion } from "framer-motion";
import ReactPlayer from "react-player";

interface VideoScrollProps {
  videoUrl: string;
}

const VideoScroll: React.FC<VideoScrollProps> = ({ videoUrl }) => {
  const videoRef = useRef<HTMLVideoElement>(null);
  const scrollYProgress = useState(0)[0];

  const handleScroll = () => {
    // const currentTime = scrollYProgress * videoRef.current?.duration ?? 0;
    // videoRef.current?.seekTo(currentTime, "seconds");
  };

  useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, [scrollYProgress]);

  return (
    <div>
      <video ref={videoRef} src={videoUrl} />
      <div style={{ height: "100vh", overflow: "auto" }}>
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          style={{
            width: "100%",
            height: "100vh",
            background: `url(${videoUrl}) no-repeat center center`,
            backgroundSize: "cover",
            transform: `translateY(-${scrollYProgress * 100}%)`,
          }}
        />
      </div>
    </div>
  );
};

export { VideoScroll };