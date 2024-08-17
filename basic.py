import tensorflow as tf
print(tf.version)

#Creating Tensors
string = tf.Variable("this is  a tensor", tf.string)
number = tf.Variable(342, tf.int16)
floating = tf.Variable(3.155, tf.float64)