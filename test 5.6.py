st = input()
if st.count('f') == 1:
    print(-1)
elif st.count('f') < 1:
    print(-2)
else:
    print(st.find('f', st.find('f') + 1))
