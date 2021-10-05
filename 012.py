input1 = []
for i in range(5):
    input1.append(int(input()))
ans = {}
parm1 = 0.08,0.1393,0.1394,1.1287,1.4803
parm2 = 0.07,0.1304,0.1217,1.1127,1.4803
parm3 = 0.06,0.1087,0.1018, 0.9572,1.1243
t = 0.0
for i in range(5):
    t = t + parm1[i]*input1[1]
ans['Type 183'] = max(t,183)
t = 0.0
for i in range(5):
    t = t + parm2[i]*input1[1]
ans['Type 383'] = max(t,383)
t = 0.0
for i in range(5):
    t = t + parm3[i]*input1[1]
ans['Type 983'] = max(t,983)
now_key = 'none'
val = 1e9
for key in ans.keys():
    if(ans[key]<val):
        now_key = key
        val = ans[key]
print(now_key,end='')
