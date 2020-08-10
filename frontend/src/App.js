import React, { useState } from 'react';
import axios from 'axios';

import { Textarea, Text, Button, Box } from '@chakra-ui/core';

function App() {
  const [text, setText] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [analyzeResult, setAnalyzeResult] = useState(null);

  const handleTextChange = (e) => {
    setText(e.target.value);
    setAnalyzeResult(null);
  };

  const handleOnClick = () => {
    setIsSubmitting(true);

    // TODO: add the correct endpoint.
    axios
      .post('/predict', {
        text,
      })
      .then(function (response) {
        console.log(response);
        // assumes that response is a number between 0.0-1.0
        setAnalyzeResult(response.data.result);
        setIsSubmitting(false);
      })
      .catch(function (error) {
        console.log(error);
        setIsSubmitting(false);
      });
  };

  return (
    <Box maxW="960px" mx="auto" padding="15px">
      <Text fontSize="5xl" as="h1">
        Fake News Classifier
      </Text>

      <Text fontSize="xl" as="p">
        Paste a news story to see how likely it is fake
      </Text>

      <Box mt="30px" mb="30px">
        <Textarea
          value={text}
          onChange={handleTextChange}
          placeholder="Type or paste your text here."
          mb="25px"
          height="300px"
        />
        <Button
          variantColor="teal"
          variant="solid"
          isLoading={isSubmitting}
          loadingText="Analyzing..."
          onClick={handleOnClick}
          disabled={text.length === 0}
        >
          Analyze text
        </Button>
      </Box>
      {analyzeResult != null && (
        <Box>
          <Text fontSize="lg" as="p">
            The model thinks that the above text is <strong>{analyzeResult * 100}%</strong> fake.
          </Text>
        </Box>
      )}
    </Box>
  );
}

export default App;
