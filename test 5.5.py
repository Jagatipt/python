st = input()
if st.count('f') == 1:
    print(st.find('f'))
elif st.count('f') >= 2:
    print(st.find('f'), st.rfind('f'))
