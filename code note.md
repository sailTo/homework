# Code Note
- features: user_id merchant_id coupon_id discount_rate distance date_received date
@   Column         Dtype  
---  ------         -----  
 0   user_id        object 
 1   merchant_id    object 
 2   action         int64  
 3   coupon_id      object 
 4   discount_rate  object 
 5   date_received  float64
 6   date           float64
offline 训练集用户与测试集用户重复数量
76307.0
offline 训练集用户与测试集重复用户在总测试集用户中的占比
0.9999737907717308
online 训练集用户与测试集用户重复数量
43155.0
online 训练集用户与测试集重复用户在总测试集用户中的占比
0.5655296229802513

## ARIMA
It can be viewed as a "cascade" of 2 models
$$
Y_t=(1-L)^dX_t
$$
$$
(1-\sum^p_{i=1}\varphi_iL^i)Y_t=(1+\sum^q_{i=1}\theta_iL^i)\varepsilon_t
$$
## func describe
|name| - | + | data|
|---|---|---|---|
|f_t_dt|Date_R,Date|Date_R,Date|of,t|
|gWD|||of,t|

g_of_f & g_on_f: add feature to test data by off & on data

## feature construct
|feature|describe|
|---|---|
|u2|用户优惠券消费次数|
|u3|用户优惠券不消费次数|
|u19|用户优惠券消费与不消费次数比值|
|u4|用户优惠券使用率|
|u5|用户普通消费次数|
|u25|用户优惠券消费和普通消费次数|
|u20|用户使用优惠券消费占比|
|u47|用户领取所有不同优惠券数量|
|u35|核销优惠券用户-商家平均距离|
|u36|用户核销优惠券中的最小用户-商家距离|
|u37|用户核销优惠券中的最大用户-商家距离|
|m0|商家销售次数|
|m1|商家优惠券核销次数|
|m2|商家普通销售次数|
|m3|商家优惠券被领取次数|
|m4|商家优惠券核销率|
|m16|商家在数据集中出现的次数|
|m20|商家被核销优惠券的平均时间|
|m21|商家被核销优惠券中的用户平均距离|
|c1|每种优惠券领取次数|
|c2|每种优惠券使用次数|
|c3|优惠券使用率|
|c6|优惠券类型|
|c12|每种优惠券核销的平均时间|
|um1|用户领取商家的优惠券次数|
|um3|用户领取商家的优惠券后核销次数|
|um4|用户领取商家的优惠券后核销率|
|o1|用户领取优惠券次数|
|on_u1|用户操作次数|
|on_u2|用户点击次数|
|on_u3|用户点击率|
|on_u4|用户购买次数|
|on_u5|用户线上购买率|
|on_u6|用户领取优惠券次数|
|on_u7|用户优惠券领取率|
|on_u9|用户优惠券消费次数|
|on_u10|用户优惠券核销率|

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNTIxNDcxNDMsODAzNjcwMDI5LDg0MT
Y3MzE0NCwxNzYwODI5NzIzLDkyNTc5NDY3NCwtNDU4NDU0MzYs
MTYxNDUyMDExMiwtMTgzMzY5MzQ3LDE5NzMxMjExNjVdfQ==
-->