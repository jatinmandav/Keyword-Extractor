import PyPDF2
import pandas as pd
import numpy as np
import sys
from collections import Counter
import argparse

from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

def read_pdf(pdf_file):
    #Reading PDF Files
    pdf_file = open(pdf_file, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    num_pages = pdf_reader.numPages
    count = 0
    text = ""
    document_text = []

    while count < num_pages:
        page_obj = pdf_reader.getPage(count)
        count += 1
        text += page_obj.extractText()
        document_text.append(text)
        text = ""

    pdf_file.close()

    return document_text

def remove_stopwords(words):
    for stopword in stop_words:
        if stopword in words:
            words = list(filter(lambda a: a != stopword, words))

    return words

def calculate_tf_idf(raw_count, max_raw_count_in_document, no_documents, no_documents_in_which_word_occured):
    tf = 0.5 + 0.5*(raw_count/max_raw_count_in_document)
    idf = np.log(no_documents/(1 + no_documents_in_which_word_occured))
    return tf*idf


parser = argparse.ArgumentParser()
parser.add_argument("--pdf_file", help="If a PDF File, the path to that file", type=str)
parser.add_argument("--text_file", help="If a TEXT file, the patht to that file", type=str)
parser.add_argument("--save_to", help="Path to CSV in to write/store Generated Keywords", default="keywords.csv", type=str)

args = parser.parse_args()

document_text = []

if args.pdf_file:
    document_text = read_pdf(args.pdf_file)
elif args.text_file:
    with open(args.text_file, 'r') as f:
        document_text.append(f.read())
else:
    print("ERROR: No File Given to read.")
    sys.exit(1)

save_to = args.save_to

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
tokenizer = RegexpTokenizer('[A-Z][a-z]\w+')

print("Generating Keywords ..")

# Tokenizing and collecting all NNPs (Proper Nouns)
for i in range(len(document_text)):
    document_text[i] = pos_tag(tokenizer.tokenize(document_text[i]))
    document_text[i] = [word[0] for word in document_text[i] if word[1].startswith("NNP")]

    document_text[i] = [word.lower() for word in document_text[i]]

# Remove all Stop words
for i in range(len(document_text)):
    document_text[i] = remove_stopwords(document_text[i])

# Lemmatizing
for i in range(len(document_text)):
    document_text[i] = [lemmatizer.lemmatize(word) for word in document_text[i]]

total_text = []

for text in document_text:
    total_text += list(text)

# Raw Count for all keywords
word_count = Counter(total_text)
raw_count = Counter(total_text)
max_raw_count_in_document = next(iter(word_count.values()))

# Calculating TF-IDF Values for all keywords
for word in word_count:
    count = 0
    for text in document_text:
        if word in text:
            count += 1

    no_documents_in_which_word_occured = count
    word_count[word] = calculate_tf_idf(word_count[word], max_raw_count_in_document, len(document_text), no_documents_in_which_word_occured)

word_count = list(word_count.items())

i = 0
for w in raw_count:
    word_count[i] = word_count[i] + (raw_count[w], )
    i += 1

# Storing all the keywords in Data-Frame
df = pd.DataFrame(list(word_count), columns=['Keywords', 'TF_IDF', "Raw_Count"])

df = df.sort_values('TF_IDF', ascending=True)
df.to_csv(save_to)

print(df.head(10))

print("Keywords saved to {}".format(save_to))
