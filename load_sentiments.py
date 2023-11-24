import pickle

if __name__ == "__main__":
	with open('tmp/sentiments.pickle', 'rb') as handle:
	    sentiments = pickle.load(handle)
	    print(len(sentiments))