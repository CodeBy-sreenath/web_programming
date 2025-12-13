def vowelcount(s):
    vowels='aeiouAEIOU'
    v_count=0
    c_count=0
    for char in s:
        if char in vowels:
            v_count+=1
        else:
            c_count+=1    
    return v_count,c_count
s="helloworld"
print("the total number of vowels and consonents are",vowelcount(s))        