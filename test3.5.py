les = int(input())
les = les*45 + (les//2)*5 + ((les+1)//2-1)*15
print(les//60 + 9, les%60)
