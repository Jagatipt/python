st = input()
a = st[:st.find('h') + 1]
b = st[st.find('h') + 1:st.rfind('h')]
c = st[st.rfind('h'):]
st = a + b.replace('h', 'H') + c
print(st)
