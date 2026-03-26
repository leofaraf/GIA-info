from math import sqrt

import matplotlib.pyplot as plt

def read_points(filename):
    pts = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                x, y = map(float, line.replace(",", ".").split('\t'))
                pts.append((x, y))
    return pts



def dist(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def dbscan(points, eps, min_pts=3):
    n = len(points)
    visited = [False] * n
    clustered = [False] * n
    clusters = []

    def region_query(i):
        return [j for j in range(n) if dist(points[i], points[j]) <= eps]

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
                    neighbors += [q for q in new_neighbors if q not in neighbors]

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

        cluster = []
        expand_cluster(i, neighbors, cluster)
        clusters.append(cluster)

    return clusters


def plot_clusters(points, clusters, title):
    plt.figure(figsize=(6, 6))

    for cluster in clusters:
        xs = [points[i][0] for i in cluster]
        ys = [points[i][1] for i in cluster]
        plt.scatter(xs, ys, s=10)

    plt.title(title)
    plt.grid()
    plt.axis("equal")
    plt.show()


points = read_points("387950_B.txt")


clusters = dbscan(points, 0.7)
plot_clusters(points, clusters, f"eps = {0.7}, clusters = {len(clusters)}")