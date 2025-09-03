## container with most water.
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

lp = 0
rp = len(height)-1
max_w = 0
while lp < rp:
    w = rp-lp
    h = min(height[lp], height[rp])
    max_w = max(max_w, w*h)

    if height[lp] < height[rp]:
        lp += 1
    else:
        rp -= 1

print(f"max contained water:{max_w}")
