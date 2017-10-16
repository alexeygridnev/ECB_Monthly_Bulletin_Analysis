import textract
import nltk
import re
import os

from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk import FreqDist

#removing stop words:
def text_stopwordfree_string(text):
    stopword_set = set(stopwords.words("english"))
    processed_tokens = ""
    for token in text.tokens:
        if (token in stopword_set): 
            processed_tokens += ""
        else:
            processed_tokens += str(token) + " "
    return processed_tokens

#removing punctuation and special characters:
def text_to_punctuationfree_string(text):
    letters_only_tokens = ""
    for tokens in text.tokens:
        letters_only_tokens += re.sub("[^a-zA-Z]",  " ", str(tokens)) + " "
    return letters_only_tokens

#converting string to an indexed text:
def string_to_text(input):
    working_text_tokens = nltk.word_tokenize(input)
    working_text = nltk.Text(working_text_tokens)
    return working_text

def process_text(file):
    pdf=textract.process(file)
    pdf=pdf.decode('utf-8')
    pdf=pdf.lower()
    print('PDF read')

    #nltk.download()

    wt=string_to_text(pdf)
    journal_length=len(wt)

    wt=text_to_punctuationfree_string(wt)
    wt=string_to_text(wt)
    print ('Punctuation removed')

    wt=text_stopwordfree_string(wt)
    wt=string_to_text(wt)
    print ('Stop words removed')

    bigrams=nltk.bigrams(wt)
    freq_bi=nltk.FreqDist(bigrams)

    colloc=freq_bi.most_common(100)
    fname=file.rstrip('.pdf')+'.csv'
    path_fin='/home/aleksei/Документы/SNS-related files/SNS_Studies/ECB Article/Monthly Bulletin/CSV files/'
    with open(os.path.join(path_fin, fname), "w") as f:
        f.write('Collocation, Amount_per_1000\n')
        for item in colloc:
            #frequency of word collocation per 10 000 words of text:
            datastr=item[0][0]+' '+item[0][1] +',' + str(item[1]/journal_length*10000)+'\n'
            f.write(datastr)
        print('File done')
path='/home/aleksei/Документы/SNS-related files/SNS_Studies/ECB Article/Monthly Bulletin/'
                    
for file in os.scandir(path):
    if file.name.endswith('.pdf'):
        process_text(file.name)



