import os
import pandas as pd
import xml.etree.ElementTree as ET
from unidecode import unidecode

def main():
    path = 'pan15-author-profiling-training-dataset-english-2015-03-02/'

    # Create dictionary with all labels
    with open(path + 'truth.txt', 'r') as f:
        lines = f.read().splitlines()

    user_labels = {}
    for line in lines:
        line.strip('/n')
        tokens = line.split(':::')
        user_labels[tokens[0]] = make_numerical(tokens[1:])


    # Read all XML documents
    files = os.listdir(path)
    files.remove('truth.txt')

    dataset = []
    for fname in files:
        tree = ET.parse(path + fname)
        root = tree.getroot()
        labels = user_labels[root.attrib['id']]
        
        for child in root:
            tweet = child.text[:-2] # Ignore last two tabs
            entry = {'user': fname[:-4],
                    'tweet': tweet,
                    'sex': labels[0],
                    'age': labels[1],
                    'ext': labels[2],
                    'sta': labels[3],
                    'agr': labels[4],
                    'con': labels[5],
                    'opn': labels[6]}
            dataset.append(entry)

    # Output results to csv file
    df = pd.DataFrame(dataset)
    df = df[['user', 'tweet', 'sex', 'age', 'ext', 'sta', 'agr', 'con', 'opn']]
    df['tweet'] = preprocess(df['tweet'])
    df.to_csv('train.csv', encoding='utf-8', index=False)


def make_numerical(labels):
    """
    Transforms text labels into numerical data.
    """
    genders = {'M': 0, 'F': 1}
    age_groups = {'18-24': 0, '25-34': 1, '35-49': 2, '50-XX': 2}

    res = []
    res.append(genders[labels[0]])
    res.append(age_groups[labels[1]])
    res.append(float(labels[2]))
    res.append(float(labels[3]))
    res.append(float(labels[4]))
    res.append(float(labels[5]))
    res.append(float(labels[6]))

    return res


def preprocess(data):
    special_chars = ' #@~'
    data = data.replace('http\S+|www.\S+', '~', regex=True)
    data = data.replace('@\S+', '@', regex=True)
    data = data.apply(lambda s: s.lower())
    data = data.apply(unidecode)
    data = data.apply(lambda s: ''.join(
                                list(map(lambda c: c if (c.isalnum() or c in special_chars) else '', s))))
    data = data.replace(' +', ' ', regex=True)
    
    return data

if __name__ == '__main__':
    main()
