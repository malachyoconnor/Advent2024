def hmm(test=set()):
     if (len(test) > 4):
        return test
     test.add(3)
     print(hmm(test))
     test.add(1000)
     print(hmm(test))
     return test


print(hmm(set()))