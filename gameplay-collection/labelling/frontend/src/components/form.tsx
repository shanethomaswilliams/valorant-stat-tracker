import React, { useState } from 'react';

interface FormProps {
  onSubmit: (url: string) => void;
}

const Form = ({ onSubmit }: FormProps) => {
  const [url, setUrl] = useState('');

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    onSubmit(url);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="url">Video URL:</label>
      <input type="text" id="url" value={url} onChange={(e) => setUrl(e.target.value)} />
      <button type="submit">Submit</button>
    </form>
  );
};

export default Form;