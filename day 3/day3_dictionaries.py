##Word Frequency WITH Manual Trace
def word_frequency(sentence=input("enter a string")):
    frequency={}
    for word in sentence.lower().split():
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
        print("word:", word, "frequency:", frequency)
word_frequency()

