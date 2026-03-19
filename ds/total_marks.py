
st = "90:34:56:87"

marks = st.split(':')
#print(marks)

total = 0
for m in marks:
    total += int(m)

print(total)