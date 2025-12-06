def merge_intervels(intervels):
    intervels.sort()
    merged=[]
    for intervel in intervels:
        if not merged or merged[-1][1]<intervel[0]:
            merged.append(intervel)
        else:
            merged[-1][1]=max(merged[-1][1],intervel[1])
    return merged
print(merge_intervels([[1,3],[2,6],[8,10]]))            
    