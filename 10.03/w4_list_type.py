# 串列 List
[57, 'banana', 'apple']     
Agroup = ['kazu', 'gorou']    # Agroup是List型別，裡面存了兩個字串型別的元素
Bgroup = ['syun', 'haruka']
Cgroup = [Agroup, Bgroup]
Cgroup[0]      #可取得Cgroup中的第一個元素(python的索引編號從0開始)
Cgroup[1][0]   #可取得Cgroup中的第二個元素中的第一個元素
print(Cgroup[0][0], ' ', Cgroup[1][1])

# 加入新元素
Agroup.append(2)     #在Agroup中新增一個元素(數值)
Bgroup.append(2)     #在Agroup中新增一個元素(數值)
print(Agroup[2] + Bgroup[2])

Agroup.append('dai')

# 刪除
Agroup.remove('dai')  # 一次只能刪除一個
Cgroup[0].remove('kazu')   #移除Cgroup第一個元素中的kazu
Cgroup[1].remove('syun')   #移除Cgroup第二個元素中的syun

# 改變順序
Agroup.sort()     #list中為數值和字串無法用sort()排序

