## Minimum Number of People to Teach
n = 3
languages = [[2],[1,3],[1,2],[3]]
friendships = [[1,4],[1,2],[3,4],[2,3]]

lang_known = {i+1: languages[i] for i in range(len(languages))}
lang_known2 = {i: list(lang_known[i]) for i in lang_known}

count = 0
for k in range(len(friendships)):
    user1 = friendships[k][0]
    user2 = friendships[k][1]
    user1_langs = lang_known[user1]
    user2_langs = lang_known[user2]

    if len(user1_langs) == 1:
        if user1_langs[0] not in user2_langs:
            lang_known2[user2].append(user1_langs[0])

    elif len(user2_langs) == 1:
        if user2_langs[0] not in user1_langs:
            lang_known2[user1].append(user2_langs[0])

    else:
        for j in range(len(user1_langs)):
            if user1_langs[j] not in user2_langs:
                lang_known2[user2].append(user1_langs[j])

count = 0
for key in lang_known:
    if lang_known[key] != lang_known2[key]:
        count += 1

print(count)
