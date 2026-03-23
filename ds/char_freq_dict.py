

st = "programming is fun, but takes effort"

d = {}   # Empty dict

for c in set(st):
    d[c] = st.count(c)

print(sorted(d.items()))