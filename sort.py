"""
使用python3版本
演示排序算法
计算排序时间
"""
import copy
import random
import time

import pylab


class ParamsError(Exception):
    """
    """
    pass


class Sorter(object):
    """
    介绍了三种排序算法
    归并，选择，冒泡
    通过模拟实验，演示排序耗时和待排数组规模的时间关系
    """
    def creat_random_list(self, length = 10000, random_list = None):
        """
        初始化一个随机数列表
        """
        self.random_list_length = length
        if random_list is None:
            self.random_list = [random.randint(0,100000) for i in range(length)]
        else:
            self.random_list = random_list

    def merge_sort(self, _list=None):
        """
        归并排序
        切分为左右两段，然后左右两段再做归并。
        典型的递归
        """
        if _list is None:
            _list = self.random_list.copy()
        length = len(_list)
        if length <= 1:
            return _list
        right = self.merge_sort(_list[:length//2])
        left = self.merge_sort(_list[length//2:])
        new_list = self.__merge(right, left)
        return new_list

    def __merge(self, right, left):
        """
        归并
        """
        rlength = len(right)
        r, l = 0, 0
        llength = len(left)
        new_list = []
        #左右两个都没空时，while循环选个小的，往队列里填元素
        while r < rlength and l < llength:
            if right[r] <= left[l]:
                new_list.append(right[r])
                r += 1
            else:
                new_list.append(left[l])
                l += 1
        #左右有一个循环完了，直接往队尾增加就行
        if r == rlength:
            new_list.extend(left[l:])
        elif l == llength:
            new_list.extend(right[r:])
        return new_list
    
    def selection_sort(self, _list=None):
        """
        选择排序，每次选择最小的移至前缀有序序列中
        """
        if _list is None:
            _list = self.random_list.copy()
        sorted = 0
        length = len(_list)
        while sorted < length:
            min = sorted
            for i in range(sorted, length):
                if _list[min] > _list[i]:#最小值小于当前值，就替换
                    min = i
            _list[sorted], _list[min] = _list[min], _list[sorted]
            sorted += 1
        return _list

    def bubble_sort(self, _list=None):
        """
        冒泡排序
        根据局部有序性来实现全局有序性
        """
        if _list is None:
            _list = self.random_list.copy()
        sorted = False
        length = len(_list)
        while not sorted:
            sorted = True
            for i in range(1, length):
                if _list[i-1] > _list[i]:#逆序的时候冒泡交换
                    _list[i-1], _list[i] = _list[i], _list[i-1]
                    sorted = False
            length -= 1#每次排序最大的必会冒到最下面
        return _list

    def get_sort_func_avg_time(self, func, times=3):
        """
        传入排序函数，执行三次，统计平均耗时
        """
        start =time.clock()
        for n in range(times):
            func()
        end =time.clock()
        avg_time = (end - start)/times
        return avg_time, self.random_list_length, func.__name__

    def run_trial(self):
        result_dict = {}
        self.length_list = [10,100,300,500,1000,2000,5000,10000,20000]
        func_list = [self.bubble_sort, self.selection_sort, self.merge_sort]
        for i in self.length_list:
            self.creat_random_list(i)
            for f in func_list:
                #key是名称，value是list
                once_res = result_dict.setdefault(f.__name__,[])
                result = self.get_sort_func_avg_time(f)
                once_res.append((result[0],result[1]))
        self.result_dict = result_dict
        return result_dict
    
    def plot_result(self):
        """
        绘制图表
        """
        tags = []
        for tag, values in self.result_dict.items():
            x = [i[1] for i in values]
            y = [i[0] for i in values]
            pylab.plot(x,y)
            tags.append(tag)
        pylab.legend(tags)
        pylab.xlabel('Array Size')
        pylab.ylabel('CPU Time')
        pylab.show()


if __name__ == "__main__":
    a = Sorter()
    a.run_trial()
    a.plot_result()
