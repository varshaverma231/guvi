abcd=set(list(map(chr, range(97, 123))))
abcd2=set(list(map(chr, range(65, 91))))
aa=abcd.union(abcd2)
i=int(input())
if i in aa:
    print("Alphabet")
else:
    print("Invalid")
