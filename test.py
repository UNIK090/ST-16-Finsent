import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required NLTK resources
nltk.download("punkt")
nltk.download("stopwords")

class TextToNum:
    def __init__(self, text):
        self.text = text
        self.cleaned = None
        self.tkns = None
        self.cl = None
        self.st = None

    def cleaner(self):
        """Cleans the text by removing punctuation and extra spaces."""
        self.text = re.sub(r',', '', self.text)
        self.text = re.sub(r'[^\w\s]', '', self.text)  # Remove special characters
        self.text = re.sub(r'\s+', ' ', self.text).strip()  # Remove extra spaces
        self.cleaned = self.text

    def token(self):
        """Tokenizes the cleaned text."""
        if self.cleaned is not None:
            self.tkns = word_tokenize(self.cleaned)
        else:
            raise ValueError("Text must be cleaned before tokenization.")

    def removeStop(self):
        """Removes stopwords from the tokenized text."""
        if self.tkns is not None:
            stop_words = set(stopwords.words('english'))
            self.cl = [word for word in self.tkns if word.lower() not in stop_words]
        else:
            raise ValueError("Text must be tokenized before removing stopwords.")

    def stemme(self):
        """Applies stemming to the filtered words."""
        if self.cl is not None:
            ps = PorterStemmer()
            self.st = [ps.stem(word) for word in self.cl]
            return self.st
        else:
            raise ValueError("Stopwords must be removed before stemming.")
