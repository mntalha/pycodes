# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 13:47:50 2021

@author: talha
"""

# This python file contains the information and explanation of tensorflow1.0 
#related subjects.

#result = softmax(weight * x +bias )
#prediction = tf.nn.softmax(tf.matmul(W,x) + b)

# bias number is the number of point that weights go

# Yani flattered olmuş halin gittiği her noktada bir bias lazım 
# cunku (w*x+b) 

#constants , variables , placeholders 
import tensorflow as tf
tf=tf.compat.v1
tf.disable_eager_execution()

# Constant
#produce ta constant output it stores

a = tf.constant(2.0)

b = tf.constant(3.0)
c = a * b

#islemleri gpu da yapmak icin session acar
sess = tf.Session()

x=sess.run(c) #degiskeni x e atar ama aynı zamanda c nin de içini doldurur.
 
#placeholder 
# run esnasında doldurmana izin veren yapı 
# tanımlandıktan sonra node sonrasında yada runtime da değişken alacağını anlar.
#constant da ilk başta tanımlaman lazımdı.

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
add = a + b
sess = tf.Session()
output = sess.run(add, {a: [1,3], b: [2, 4]})

#(<number of images>, <image x_dim>, <image y_dim>, <number of channels>)
