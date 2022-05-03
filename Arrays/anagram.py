
anagrams = ['cat', 'dog', 'fired', 'god', 'pat', 'tap', 'fried', 'tac']
def anagram(list):
    d={}
    for s in anagrams:
        sorted_s=str(sorted(s))
        if sorted_s in d:
            d[sorted_s].append(s)
        else:
            d[sorted_s]=[s]
    return d
  
  
  
  # second
  def anagram(list):
    are_anagrams = lambda x, y: str(sorted(x.lower())) == str(sorted(y.lower()))
    for i in range(len(anagrams)):
        for j in range(len(anagrams)):
            if are_anagrams(anagrams[i],anagrams[j]):
                print(anagrams[i],anagrams[j])
