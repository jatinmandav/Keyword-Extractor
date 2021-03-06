## Keyword-Extractor
Keyword extraction is tasked with the automatic identification of terms that best describe the subject of a document ([More on Wikipedia](https://en.wikipedia.org/wiki/Keyword_extraction)).

### Requirements
  - [PyPDF2](https://github.com/mstamy2/PyPDF2) - A utility to read and write PDF files in Python `pip3 install PyPDF2`
  - [Pandas](https://github.com/pandas-dev/pandas) - For saving data in DataFrame `pip3 install pandas`
  - [NumPy](https://github.com/numpy/numpy) - For Mathematics (IF-IDF) `pip3 install numpy`
  - [NLTK](https://github.com/nltk/nltk) - Tokenizing, Lemmatizing, Part-of-Speech Taggin etc `pip3 install nltk`

### Usage
 - Get the Repository
 
 `git clone https://github.com/jatinmandav/Keyword-Extractor`
 
 - Change Directory to Keyword-Extractor
 
 `cd Keyword-Extractory`
 
 - $ python3 extract_keywords.py --help
 ```
 $ python3 extract_keywords.py --help

usage: extract_keywords.py [-h] [--pdf_file PDF_FILE] [--text_file TEXT_FILE] [--save_to SAVE_TO]

optional arguments:
-h, --help             show this help message and exit
--pdf_file PDF_FILE    If a PDF File, the path to that file
--text_file TEXT_FILE  If a TEXT file, the patht to that file
--save_to SAVE_TO      Path to CSV in to write/store Generated Keywords | Deafult: keywords.csv
```

## Algorithm
  - [Read PDF or TEXT file](https://github.com/jatinmandav/Keyword-Extractor/blob/0b573449c5b016e422e17e803d999857ce6bdadb/extract_keywords.py#L13). (For PDF files, each page is treated as a single document which helps in weighting the keywords)
  
  - [Tokenization](https://github.com/jatinmandav/Keyword-Extractor/blob/13904fb8f01ee6ff493f7d19f32e1d6a0fa962ab/extract_keywords.py#L69): The text is then tokenized using `RegexpTokenizer` from `nltk.tokenize`, allowing only Alphabets, [A-Z] and [a-z] thus also removing puncutations from the text.
  
  - [Part-of-Speech Tagging](https://github.com/jatinmandav/Keyword-Extractor/blob/13904fb8f01ee6ff493f7d19f32e1d6a0fa962ab/extract_keywords.py#L73): The tokenized text is then tagged using `pos_tag` from `nltk.tag`. After tagging the complete text, only the Proper Nouns (singular(NNP) and plural(NNPS)) are collected.
  
  - [Removing Stopwords](https://github.com/jatinmandav/Keyword-Extractor/blob/13904fb8f01ee6ff493f7d19f32e1d6a0fa962ab/extract_keywords.py#L80): Next the stopwords from `nltk.corpus` are removed from the text as they do not really contriute towards explaining the document.
  
  - [Lemmatizing](https://github.com/jatinmandav/Keyword-Extractor/blob/13904fb8f01ee6ff493f7d19f32e1d6a0fa962ab/extract_keywords.py#L84): The words are them lemmatized using `WordNetLemmatizer` from `nltk.stem` thus only storing the root words.
  
  - [Raw Count](https://github.com/jatinmandav/Keyword-Extractor/blob/13904fb8f01ee6ff493f7d19f32e1d6a0fa962ab/extract_keywords.py#L93): Using `Counter()` from `collections`, the raw count of each word in calculated.
  
  - [Calculating TF-IDF scores](https://github.com/jatinmandav/Keyword-Extractor/blob/13904fb8f01ee6ff493f7d19f32e1d6a0fa962ab/extract_keywords.py#L41): 
    - TF Value: Augmented Frequency, to prevent a bias towards longer documents, e.g. raw frequency divided by the raw frequency of the most occurring term in the document
      
      - `tf = 0.5 + 0.5*(raw_count/max_row_count_in_document)`
    
    - IDF Value: Logarithmically scaled inverse fraction of the documents that contain the word, obtained by dividing the total number of documents by the number of documents containing the term, and then taking the logarithm of that quotient.
    
      - `idf = log(no_documents/(1 + no_documents_in_which_word_occured))`
      
    - [TF-IDF Value](https://en.wikipedia.org/wiki/Tf%E2%80%93idf): tf*idf
    
  - [Sorting and Storing the data with respect to tf-idf scores](https://github.com/jatinmandav/Keyword-Extractor/blob/13904fb8f01ee6ff493f7d19f32e1d6a0fa962ab/extract_keywords.py#L116).
    
