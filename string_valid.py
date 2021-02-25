s = 'googleavaskdjfdlfskjdlknnkkkkkk'


counter = []
set_s = set(s)
for c in set_s:
    counter.append(s.count(c))

a = zip(counter, set_s)
a_sorted = sorted(a, key=lambda a: a[0])
b = a_sorted[-1:-4:-1]

for c in a_sorted[-1:-4:-1]:
    print(f'{c[1]} {c[0]}')

print("end")