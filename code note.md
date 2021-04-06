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

g_of_f & g_on_f: add feature to test data by off & on data
<!--stackedit_data:
eyJoaXN0b3J5IjpbODQxNjczMTQ0LDE3NjA4Mjk3MjMsOTI1Nz
k0Njc0LC00NTg0NTQzNiwxNjE0NTIwMTEyLC0xODMzNjkzNDcs
MTk3MzEyMTE2NV19
-->