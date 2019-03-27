import os
import pandas as pd
import xml.etree.ElementTree as ET

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
            tweet = child.text[:-2].casefold() # Casefold and ignore last two tabs
            entry = {'tweet': tweet,
                    'gender': labels[0],
                    'age_group': labels[1],
                    'extraversion': labels[2],
                    'neuroticism': labels[3],
                    'agreeableness': labels[4],
                    'conscientiousness': labels[5],
                    'openness': labels[6]}
            dataset.append(entry)

    # Output results to csv file
    df = pd.DataFrame(dataset)
    df = df[['tweet', 'gender', 'age_group', 'extraversion', 'neuroticism', 'agreeableness', 'conscientiousness', 'openness']]
    df = preprocess(df)
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
    data = data.replace('http\S+|www.\S+', '~', regex=True)
    data = data.replace('@\S+', '@', regex=True)
    
    return data

if __name__ == '__main__':
    main()
