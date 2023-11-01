// src/api.ts
export async function fetchImageFilenames(
  imageDataPath: string
): Promise<string[]> {
  const imageResponse = await fetch(imageDataPath);
  const imageText = await imageResponse.text();
  const imageFilenames = imageText
    .split("\n")
    .filter((filename) => filename.trim() !== "");

  return imageFilenames;
}
