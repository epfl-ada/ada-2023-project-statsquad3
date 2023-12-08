import numpy as np


# Methods for score analysis

# Adjust score with the lexicon
def method1_1(text, score, positive_words, negative_words, max_adjustment=0.5):
    words = text.split()
    positive_count = sum(word in positive_words for word in words)
    negative_count = sum(word in negative_words for word in words)

    if abs(score) >= 0.2:
        difference = positive_count - negative_count
        adjustment = (np.log(abs(difference) + 1) / np.log(max_adjustment + 1)) * np.sign(difference)
        adjustment = np.clip(adjustment, -max_adjustment, max_adjustment)
    else:
        return score

    score += adjustment
    score = np.clip(score, -1, 1)
    return score


# Ajust the score based on the ratio of positive/negative score
def method1_2(pos,neg):   
    if pos>=neg:
        final_score=1-(neg/pos)
    else:
        final_score=-1+(pos/neg)

    return final_score


#-----------------------------------------------
# Methods for path analysis

# Only return the direct path, remove the articles that the player comeback from
def method2_1(path):

    list1=path.split(';')

    while '<' in list1:
        idx=list1.index('<')-1
        list1=list1[:idx]+list1[idx+1:]
        list1.remove('<')

    return list1


# Return the total path, replace < by the actual article
def method2_2(path):
    list1=path.split(';')

    while '<' in list1:
        i=1
        idx=list1.index('<')
        try:
            while list1[idx+i]=='<':
                i=i+1
        except:
            None
        list1[idx+i-1]=list1[idx-1-i]

    return list1