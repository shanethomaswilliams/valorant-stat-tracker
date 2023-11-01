// src/ImageViewer.tsx
import React, { useState, useEffect } from "react";
import { fetchImageFilenames } from "../utilities/api";

interface ImageViewerProps {
  imageDataPath: string;
}

const ImageViewer: React.FC<ImageViewerProps> = ({ imageDataPath }) => {
  const [imageFilenames, setImageFilenames] = useState<string[]>([]);
  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  useEffect(() => {
    async function fetchImages() {
      const filenames = await fetchImageFilenames(imageDataPath);
      setImageFilenames(filenames);
    }
    fetchImages();
  }, []);

  const currentImage = imageFilenames[currentImageIndex];

  const handleNext = () => {
    setCurrentImageIndex(
      (prevIndex) => (prevIndex + 1) % imageFilenames.length
    );
  };

  return (
    <div>
      {currentImage && (
        <img
          src={`${imageDataPath}/${currentImage}`}
          alt="Current"
          style={{ maxWidth: "100%" }}
        />
      )}
      <button onClick={handleNext}>Next</button>
    </div>
  );
};

export default ImageViewer;
