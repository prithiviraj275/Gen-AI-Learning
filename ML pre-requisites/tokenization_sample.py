import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt_tab')
txt = "Hello world. This is a test sentence. Tokenization is important in NLP."
sentences = sent_tokenize(txt)
print(sentences)