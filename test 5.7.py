st = input()
st = st[:st.find('h')] + st[st.rfind('h') + 1:]
print(st)
