category_columns = ['US_aaa', 'NL_bbb']
new = []
for c in category_columns:
    if '_' in c:
        c = c[3:]
        # new.append(c[3:])

print(category_columns)
print(new)