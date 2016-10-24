import Node


class KD:
    def __init__(self,points,dimension_num,Range,n):
        self.root = Node(points,dimension_num)
        self.root.Range = Range
        self.dimension_num = dimension_num
        self.n = n
        if self.n > 0:
            self._buildKD()

    def _buildKD(self):
        self.split=self.root.d_max_duc
        middle = sum(self.Range[self.split]) / 2
        l_points=[p for p in self.points if p[self.split]<=middle]
        r_points=[p for p in self.points if p[self.split]> middle]
        l_range=[i[:] for i in self.Range[:]]
        l_range[self.split][1] = middle
        r_range=[i[:] for i in self.Range[:]]
        r_range[self.split][0] = middle

        self.root.lchild=KD(l_points,self.dimension_num,l_range,self.n-1).root
        self.root.rchild=KD(r_points,self.dimension_num,r_range,self.n-1).root

    def _getMiddle(self):
        return sum(self.Range[self.split])/2

    def get(self,point):
        current = self
        while current.n > 0:
            middle = current._getMidlde()
            if point[current.root.split] <= middle:
                current = current.root.lchild
            else:
                current = current.root.rchild
        if len(current.root.points)==0:
            return 0,"abnormal"

        min_distance = current._get_min_distance(point)
        return 1,min_distance

    def _get_min_distance(self,point):
        min_distance = self._get_distance(point,self.points[0])
        for p in self.points[1:]:
            new_distance = self._get_distance(point,p)
            if min_distance > new_distance :
                min_distance = new_distance
        return min_distance

    def _get_distance(self,p1,p2):
        diff = [(p1[i]-p2[1])**2 for i in xrange(len(p1))]
        sum_diff = sum(diff)
        return sum_diff

