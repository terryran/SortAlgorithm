# 本脚本实现三个常见排序算法，通过图例展示不同排序算法的时间复杂度
## 执行结果
  ![image](https://github.com/terryran/SortAlgorithm/blob/master/images/Figure_1.png)
## 原因分析
### 归并排序
  时间复杂度为nlogn.较大数组量情况下确实为最小。
  但是可以发现，数据量较小时，耗时反而更高。
  ![image](https://github.com/terryran/SortAlgorithm/blob/master/images/Figure_2.png)
  原因时归并排序需要开辟新的内存空间存储，开辟存储空间的耗时大于其余就地排序时间。
### 选择排序和冒泡排序
  时间复杂度都是n^2,但是选择排序选择排序耗时远低于冒泡排序。
  通过对比源码85行和103行可以发现。两种排序策略的交换方式不一致，选择排序交换次数平均会小于冒泡排序次数。
  可以发现选择排序复杂度常数项较低。