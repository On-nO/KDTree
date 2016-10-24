class Node:
    def __init__(self,points,dimension_num,parent=None,lchild=None,rchild=None, Range=None, Split=None):
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild
        self.Range = Range
        self.Split = Split
        self.points=points
        self.dimension_num=dimension_num
        self.d_max_duc=self.get_d_max_duc()

    def get_d_max_duc(self):
        # 具有最大延展度的维度
        # 延展度 ductility
        d_max_duc=0
        max_duc=self._get_duc(0)
        for d in xrange(1,self.dimension_num):
            new_duc = self._get_duc(d)
            if max_duc < new_duc:
                max_duc = new_duc
                d_max_duc=d
        return d_max_duc

    def _get_duc(self,dimension_num):
        lst=sorted(self.points,key=lambda p:p[dimension_num])
        return abs(lst[0][dimension_num]-lst[-1][dimension_num])
