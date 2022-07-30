class Solution:
    def get_dist(self, point1, point2):
        return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dist_set = []
        dist_set.append(self.get_dist(p1, p2))
        dist_set.append(self.get_dist(p1, p3))
        dist_set.append(self.get_dist(p1, p4))
        dist_set.append(self.get_dist(p2, p3))
        dist_set.append(self.get_dist(p2, p4))
        dist_set.append(self.get_dist(p3, p4))
        dist_set = sorted(dist_set)
        if dist_set[0] == dist_set[1] == dist_set[2] == dist_set[3] and \
        dist_set[3] != dist_set[4] and \
        dist_set[4] == dist_set[5]:
            return True
        return False