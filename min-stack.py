class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.data) > 0:
            pre_value, pre_min = self.data[-1]
            if x < pre_min:
                pre_min = x
        else:
            pre_min = x

        self.data.append((x, pre_min))

    def pop(self):
        """
        :rtype: None
        """
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.data[-1][1]
