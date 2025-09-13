## Minimum Number of People to Teach
n = 4
languages = [[1],[2],[3],[4]]
friendships = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

lang_known = {i+1: set(languages[i]) for i in range(len(languages))}
need_teach = set()
for u, v in friendships:
    if lang_known[u] & lang_known[v]:
        continue
    need_teach.add(u)
    need_teach.add(v)
 
freq = [0] * (n+1)
for person in need_teach:
    print(need_teach)
    for lang in lang_known[person]:
        print(lang)
        freq[lang] += 1
        
max_known = max(freq)
print(freq)
print(len(need_teach) - max_known)