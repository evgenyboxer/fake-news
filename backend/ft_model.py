import os
import pickle

import numpy as np

from typing import Optional

from backend.utils import common

from tensorflow.keras import models
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence

class NNClassifier:
    MODEL_NAME: str = 'fake_news_keras'
    MAX_FEATURES: int = 10000    # number of words to consider as features
    MAXLEN: int = 200            # cut off the text after this number of words
                                 # (among the MAX_FEATURES most common words)
    EMB_DIM: int = 100           # embedding dimension

    def __init__(self, text: str) -> None:
        self.raw_text = text
        self._model: Optional[models.Model] = None
        self._tokenizer: Optional[Tokenizer] = None
        common.logger.info(f'NNClassifier initialized')

    @property
    def _model_path(self) -> str:
        return os.path.join(common.PROJECT_FOLDER, f'data/{self.MODEL_NAME}.h5')

    def _preprocess(self) -> np.ndarray:
        if self._tokenizer is None:
            self.load_model()
        pred_sequence: np.ndarray = np.array(self._tokenizer.texts_to_sequences(np.array([self.raw_text])))
        pred_sequence = sequence.pad_sequences(pred_sequence, maxlen=self.MAXLEN)
        return pred_sequence

    def load_model(self) -> None:
        self._model = models.load_model(self._model_path)
        common.logger.info(f'Model loaded successfully from {self._model_path}')

        with open('./data/tokenizer.pickle', 'rb') as f:
            self._tokenizer = pickle.load(f)
        common.logger.info(f'Tokenizer loaded successfully')

    @property
    def model(self) -> models.Model:
        if self._model is None:
            self.load_model()
        return self._model

    def predict(self) -> float:
        seq = self._preprocess()
        pred = self._model.predict(seq)
        return round(float(pred[0][0]), 3)
