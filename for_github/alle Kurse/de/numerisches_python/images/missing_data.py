s = str(fac(900))
for start, l in [(387, 12), (589, 24), (1410, 15), (1850, 27)]:
    s = s[:start] + '\x1b[6;30;42m' + "?"*l + '\x1b[0m' + s[start+l:]
