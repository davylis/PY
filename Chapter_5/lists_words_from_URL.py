from urllib.request import urlopen

def lists_words_from_url():

    #fetch the world list
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    word_list = urlopen(url).read().splitlines()

    count=len(word_list)

    #average word length
    total_length=sum(len(w) for w in word_list)
    average_length=total_length/count

    #Initialize counters for word lengths(1-22)
    counters = [0] * 23

    #count words based on their length
    for w in word_list:
        word_length=len(w)
        if 1<=word_length<=22:
            counters[word_length]+=1

    #result
    print(str(count)+" words")
    print(f"The average word length is {average_length:.2f}")
    print("Length Count")
    for l in range(1,23):
        print(f" {l:>5} {counters[l]:>5}")

lists_words_from_url()


