
def palindrome(s):
    i,j=0,len(s)-1

    while i<=j:
        if s[i]!=s[j]: return False
        i+=1
        j-=1

    return True

def partitoning(idx,s,ans,sub):

    if idx>=len(s):
        ans.append(sub.copy())
        return

    for i in range(idx,len(s)):
        word=s[idx:i+1]
        print(word)
        if palindrome(word):
            sub.append(word)
            partitoning(i+1,s,ans,sub)
            sub.pop()


s='aab'
ans=[]
sub=[]
partitoning(0,s,ans,sub)
print(ans)
