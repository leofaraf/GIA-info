from math import sqrt

def read_points(filename):
    pts = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                x, y = map(float, line.replace(",",".").split())
                pts.append((x, y))
    return pts

def dist(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def dbscan(points, eps, min_pts=3):
    n = len(points)
    visited = [False] * n
    clustered = [False] * n
    clusters = []

    def region_query(i):
        neighbors = []
        for j in range(n):
            if dist(points[i], points[j]) <= eps:
                neighbors.append(j)
        return neighbors

    def expand_cluster(i, neighbors, cluster):
        cluster.append(i)
        clustered[i] = True

        k = 0
        while k < len(neighbors):
            j = neighbors[k]

            if not visited[j]:
                visited[j] = True
                new_neighbors = region_query(j)
                if len(new_neighbors) >= min_pts:
                    for q in new_neighbors:
                        if q not in neighbors:
                            neighbors.append(q)

            if not clustered[j]:
                cluster.append(j)
                clustered[j] = True

            k += 1

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        neighbors = region_query(i)

        if len(neighbors) < min_pts:
            continue
        else:
            cluster = []
            expand_cluster(i, neighbors, cluster)
            clusters.append(cluster)

    return clusters


def cluster_center(cluster_points):
    best_point = None
    best_sum = float('inf')

    for p in cluster_points:
        s = 0
        for q in cluster_points:
            s += dist(p, q)
        if s < best_sum:
            best_sum = s
            best_point = p

    return best_point


def cluster_radius(cluster_points):
    center = cluster_center(cluster_points)
    r = 0
    for p in cluster_points:
        r = max(r, dist(center, p))
    return r


def solve(filename, eps, min_pts=3):
    points = read_points(filename)
    clusters_idx = dbscan(points, eps, min_pts)

    clusters = []
    for cl in clusters_idx:
        clusters.append([points[i] for i in cl])

    radii = [cluster_radius(cl) for cl in clusters]
    R = sum(radii) / len(radii)

    return abs(int(R * 10000)), radii, len(clusters)


ansA, radiiA, cntA = solve("387950_A.txt", eps=0.7, min_pts=3)
ansB, radiiB, cntB = solve("387950_B.txt", eps=0.7, min_pts=3)

print(ansA, radiiA, cntA)
print(ansB, radiiB, cntB)