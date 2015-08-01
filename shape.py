#! /usr/bin/env python3
from curve import *
from instance import *
plt.axis('equal')
hold(True)
rp=0.03
#测试旋转平移等功能的正确性
c1,c2=curve7()
t1=-0.35
t2=1.65
ce1=rotc(c1,t1*uni)
ce2=rotc(c2,t2*uni)
#drawc(ce1)
#drawc(ce2)
r1=closest(ce1,ce2,rp)
draw2(ce1,ce2,r1,rp)
plt.axis('off')
#plt.clf()
savefig('shape.pdf')
print('Terminated Normally!')
