def totalFruit(fruits):
    left=0
    maxWindowSize=0
    fruitsHash={}

    for right in range(len(fruits)):
        if fruits[right] not in fruitsHash:
           fruitsHash[fruits[right]]=0
        fruitsHash[fruits[right]]+=1
        maxWindowSize+=1

        while len(fruitsHash)>2:
            fruitsHash[fruits[left]]-=1

            if fruitsHash[fruits[left]]==0:
                del fruitsHash[fruits[left]]

            left+=1
            maxWindowSize-=1

    return maxWindowSize

print(totalFruit([1,2,3,2,2]))

        