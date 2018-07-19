## Keyword-Extractor
Keyword extraction is tasked with the automatic identification of terms that best describe the subject of a document.

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
 
```$ python3 extract_keywords.py --help

usage: extract_keywords.py [-h] [--pdf_file PDF_FILE] [--text_file TEXT_FILE] [--save_to SAVE_TO]

optional arguments:
-h, --help             show this help message and exit
--pdf_file PDF_FILE    If a PDF File, the path to that file
--text_file TEXT_FILE  If a TEXT file, the patht to that file
--save_to SAVE_TO      Path to CSV in to write/store Generated Keywords | Deafult: keywords.csv```






