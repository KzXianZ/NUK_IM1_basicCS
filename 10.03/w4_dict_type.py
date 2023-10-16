# 字典 Dictionary Type (DICT)
_class = {'1stclass': 65, '2ndclass': 55, '3rdclass': 45}
_class['1stclass']
_class['2ndclass']
_class['3rdclass']
print(_class['1stclass'] + _class['2ndclass'] + _class['3rdclass'])


activities = {'Monday':'籃球', 'Tuesday':  
         '自行車', 'Wednesday':'輕音樂', 
              'Friday':'游泳'}
activities['Tuesday']
activities['Friday']
print(activities['Monday'], activities['Friday'])

#List與Dictionary結合
l1 = [150, '奶茶', '漢堡']
l2 = [200, '牛奶', '沙拉']
l3 = [120, '果汁', '拉麵']
l3.append('糖果')
ep = {'1':l1, '2':l2, '3':l3}
ep['1']
ep['2']
ep['3']
print(ep['1'][0] + ep['2'][0] + ep['3'][0])   #將三天花費總額相加

activities = {'Monday':5, 'Tuesday':6, 'Wednesday':4, 
              'Friday':3}
print(activities['Monday'] + activities['Friday'])
print(20-(activities['Monday'] + activities['Tuesday']\
          + activities['Wednesday'] + activities['Friday']))

activities = {1:'籃球', 2:'自行車', 3:'輕音樂', 4:'游泳'}


activities.keys()
activities.values()
