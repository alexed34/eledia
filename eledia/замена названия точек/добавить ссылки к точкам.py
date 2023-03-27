from point_url import d
# print(d)
with open('text_replace.txt', 'r', encoding='utf-8') as f:
    file = f.read()


# print(file.split())
for i in file.split():
    # print(i)
    if i in d:
        t = f"<a href={d[i]}>{i}</a>"
        # print( f"<a href={d[a]}>{a}</a>")
        # print(t)
        file = file.replace(i, t)


# for k, v in d.items():
#     file = file.replace(k, f"<a href={v}>{k}</a>")
print(file)