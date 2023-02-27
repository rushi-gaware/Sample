# Q. Define a function to check the given words are anagrams or not

def anagrams (a1,a2) :
        if sorted(a1) == sorted(a2):
            print('\n\n'"The String is Anagrms")
        else :
            print('\n\n'"THe word is not an Anagram")
            

a1 = input ("Enter the 1st word : ")
a2 = input ("Enter the seconf word : ")

anagrams (a1,a2)