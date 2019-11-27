'''
import numpy as np
np.__version__
#l = list(range(10))
#l
#type(l[0])
l2 = [str(c)for c in l]
l2
type(l2[0])
import array
l = list('a','s','f')
a = array.array('u',l)
type(a[0])
np.array([1,2,4,5,3.2,'my',True])
#multidimensional array
np.array([range(i,i+3) for i in [2,4,6]])
np.zeros(10,dtype=int)
np.ones((4,5),dtype=float)
np.full((3,5),3.14)
l3 = [True, '2', 2.0,4]
[type(item)for item in l3]
#fixed type i,Q,q,b,B,d=integer,f=float,u=char
import array
l = list(range(10))
a = array.array('i',l)
anp.array([True,3.14,2,], dtype = 'float')
np.arange(0,20,3)
np.linspace(0,3,9)
=array([0.   , 0.375, 0.75 , 1.125, 1.5  , 1.875, 2.25 , 2.625, 3.   ])
np.random.random((3,4))
Module,class,function
np.random.normal(0,1,(3,3))
np.random.randint(0,10,(3,3))
np.eye(3)
np.empty(3)
m = np.ones((2,3))
m
n = np.arange(1,3)
np.empty(3)
em = np.empty(3)
em.put(2,3,mode='raise') =change values from 0-2
em
'''