import tensorflow as tf
import numpy


#Creating Tensors
string = tf.Variable("this is  a tensor", tf.string)
number = tf.Variable(342, tf.int16)
floating = tf.Variable(3.155, tf.float64)


#Rank/Degree of tensors
#Basically the number of dimension involved in the tensor
#The above tensors are rank 0 or they are scaler

#Creating some high Degree tensor
rank1_tensor = tf.Variable(["Test1"], tf.string)
rank2_tensor = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)

#To determine the rank we call the following method
rank1 = tf.rank(rank1_tensor)
print(rank1)
#Its basically the deepest level of the nested list or array

#Shape of the tensor
#Its basically the number of the elements that exist in each dimension

shapeT = rank2_tensor.shape
print(shapeT)

#reshaping a tensor
tensor1 = tf.ones([1,2,3])  # tf.ones() creates a shape [1,2,3] tensor full of ones
print(tensor1)
#tf.Tensor(
#[[[1. 1. 1.] now the shape in 1,2,3 how it works is that we have one interior list inside that 2 list and inside all those list 3 elements
 # [1. 1. 1.]]], shape=(1, 2, 3), dtype=float32)

tensor2 = tf.reshape(tensor1, [2,3,1])
#same logic this will create 2 interior list then 3 list inside that and each of them would have one element
print(tensor2)

tensor3 = tf.reshape(tensor2, [3,-1]) # -1 tells the tensor to calculate the size of the dimension in that place
                                      # this will reshape the tensor to [3,2]
#so we know that it have 6 elements so to have a valid shape the product of all three should be six to have a valid shape