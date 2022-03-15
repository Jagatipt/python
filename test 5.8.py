st = input()
a = st[:st.find('h')]
b = st[st.find('h'):st.rfind('h') + 1]
c = st[st.rfind('h') + 1:]
st = a + b[::-1] + c
print(st)
