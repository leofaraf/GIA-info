from math import sqrt

points = []
with open('387950_A.txt', encoding='utf-8') as f:
    for line in f:
        x, y = line.strip().split('\t')
        points.append((float(x.replace(',', '.')), float(y.replace(',', '.'))))

cluster1 = [p for p in points if p[0] < 3]
cluster2 = [p for p in points if p[0] >= 3]

def dist(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def radius(cluster):
    center = min(cluster, key=lambda p: sum(dist(p, q) for q in cluster))
    return max(dist(center, q) for q in cluster)

r1 = radius(cluster1)
r2 = radius(cluster2)
R = (r1 + r2) / 2

print(int(abs(R * 10000)))