def checkInclusion(s1, s2):
    left=0
    hash={}
    matched=0
    for i in range(len(s1)):
        if s1[i] not in hash:
            hash[s1[i]]=0
        hash[s1[i]]+=1

    for right in range(len(s2)):
        
        rightChar=s2[right]
        if rightChar in hash:
            hash[rightChar]-=1
            if hash[rightChar]==0:
                matched+=1
            
        if matched==len(hash):
            return True

        if right-left>=len(s1)-1:
            leftChar=s2[left]
            left+=1
            if leftChar in hash:
                if hash[leftChar]==0:
                    matched-=1
                hash[leftChar]+=1

    return False

print(checkInclusion("abc","acab"))
