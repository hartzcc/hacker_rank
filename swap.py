string = 'ABCDCDC'
sub_string = 'CDC'



ctr = 0
end = len(sub_string)
for i, _ in enumerate(string):
    if string.find(sub_string, i, i + end) != -1:
        ctr += 1

print(ctr)