abcd=set(list(map(chr, range(97, 123))))
abcd2=set(list(map(chr, range(65, 91))))
aa=abcd.union(abcd2)
a=input()
if a in aa:
    if a in ['a','e','o','i','u','A','E','O','I','U']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
