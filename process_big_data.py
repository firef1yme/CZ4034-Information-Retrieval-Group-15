import pandas as pd

def main():
    with open('100g.all', 'r') as f:
        lines = f.read().splitlines()
            
    dataset = []
    labels = {'m': 0, 'f': 1, 'E': 0, 'I': 1, 'S': 0, 'N': 1, 'T': 0, 'F': 1, 'J': 0, 'P': 1}
    for line in lines:
        personality, gender, _, text = line.strip().split("\t", 4)
        text = preprocess(text)

        entry = {'tweet': text,
                 'm/f': labels[gender],
                 'e/i': labels[personality[0]],
                 's/n': labels[personality[1]],
                 't/f': labels[personality[2]],
                 'j/p': labels[personality[3]]}
        dataset.append(entry)

    # Output results to csv file
    df = pd.DataFrame(dataset)
    df = df[['tweet', 'm/f', 'e/i', 's/n', 't/f', 'j/p']]
    df.to_csv('big_train.csv', encoding='utf-8', index=False)
    print(df['tweet'])


def preprocess(text):
    res = ''
    chars_to_skip = 0
    
    for word in text.split(' '):
        if chars_to_skip > 0:
            chars_to_skip -= len(word)
        else:
            if word == '@URL':
                # URLs are followed by 10 random characters, ignore these
                chars_to_skip = 10
                res += '~. '
            elif word == '@USER':
                res += '@ '
            elif word == '@HASHTAG':
                res += '# '
            else:
                res += word + ' '

    return res[:-1].lower() # Skip last space character


    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
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
            entry = {'tweet': tweet,
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
    df = df[['tweet', 'sex', 'ei', 'sn', 'tf', 'jp']]
    df = preprocess(df)
    df.to_csv('big_train.csv', encoding='utf-8', index=False)"""


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


if __name__ == '__main__':
    main()
