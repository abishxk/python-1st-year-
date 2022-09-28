marks={'ravi':[97,85,86,78],'rahul':[94,92,95,91]}
tot=0
totmarks=marks.copy()

for key,val in marks.items():
    tot=sum(val)
    totmarks[key]=tot
    print(totmarks)

    max=0
    topper=' '

for key,val in totmarks.items():
    if val>max:
        max=val
        topper=key
print('topper is',topper,'with marks',max)
