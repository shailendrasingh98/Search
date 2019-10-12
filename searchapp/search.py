from operator import itemgetter

# map to store words and correponding frequency
word_freq = {}
# to store unique words available
words = set()
# opening the tab sepearted seed  data file
with open('word_search.tsv') as datafile:
	for row in datafile:
		word, frequency = row.split('\t')
		word_freq[word] = int(frequency.strip())
		words.add(word)

# search words for match in seed data
def search(patial_word):
    '''generator to return words containing partial inputted word or string'''
    for word in words:
        if patial_word in word:
            yield word

def _weightedSort(data):
    # matches at the start of a word should be ranked higher
    data.sort(key=itemgetter(1))
    # Sort based on the frequency
    data.sort(key=itemgetter(2), reverse = True)
    # Sort based on lenght keeping match at start at higher rank
    data.sort(key=itemgetter(1, 3))
    return data

def sorting(data, patial_word):
    '''sorts the words based on a match with the search keyword'''
    word_distances = [(word, word.find(patial_word), word_freq[word], len(word)) for word in data]
    return [word_distance[0] for word_distance in _weightedSort(word_distances)][:25]

if __name__ == '__main__':
    print(search('pra')[:25])
