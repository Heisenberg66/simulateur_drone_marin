import numpy as np
import pygame
import tensorflow as tf
from sklearn.model_selection import train_test_split
import time
from make_sonar_combinaison import make_combinaisons
from gen_verite_terrain import make_truth

class Neural_network(object):

	def __init__(self,sc,l_c,v_t):
		self.screen =sc
		self.liste_combinaison = l_c
		self.verite_terrain = v_t
		self.train_dataset, self.test_dataset, self.train_labels, self.test_labels = train_test_split(
     		self.liste_combinaison, self.verite_terrain, test_size = .1, random_state = 12)
		self.n_nodes_hl1 = 50
		self.n_nodes_hl2 = 50
		self.n_nodes_hl3 = 50
		self.num_labels = self.train_labels.shape[1]  #num_labels = 10
		self.batch_size = 1
		self.num_features = self.train_dataset.shape[1] #num_features = 30
		self.graph = tf.Graph()
		self.tf_train_dataset = None
		self.tf_train_labels = None
		self.tf_test_dataset = None
		self.model_scores=None
		self.loss = None
		self.optimizer = None
		self.train_prediction = None
		self.test_prediction = None


	def setup_network(self):


		with self.graph.as_default():	
			
			self.tf_train_dataset = tf.placeholder(tf.float32, shape = [None, self.num_features])
			self.tf_train_labels = tf.placeholder(tf.float32, shape = [None, self.num_labels])
			self.tf_test_dataset = tf.constant(self.test_dataset)
    
			def three_layer_network(data):

				hidden_1_layer = {'weights':tf.Variable(
					tf.truncated_normal([self.num_features, self.n_nodes_hl1])),'biases':tf.Variable(tf.zeros([self.n_nodes_hl1]))}
				hidden_2_layer = {'weights':tf.Variable(
					tf.truncated_normal([self.n_nodes_hl1, self.n_nodes_hl2])),'biases':tf.Variable(tf.zeros([self.n_nodes_hl2]))}
				hidden_3_layer = {'weights':tf.Variable(
					tf.truncated_normal([self.n_nodes_hl2, self.n_nodes_hl3])),'biases':tf.Variable(tf.zeros([self.n_nodes_hl3]))}
				output_layer = {'weights':tf.Variable(
					tf.truncated_normal([self.n_nodes_hl3, self.num_labels])),'biases':tf.Variable(tf.zeros([self.num_labels])),}
    	


				l1 = tf.add(tf.matmul(data,hidden_1_layer['weights']), hidden_1_layer['biases'])
				l1 = tf.nn.relu(l1)

				l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights']), hidden_2_layer['biases'])
				l2 = tf.nn.relu(l2)

				l3 = tf.add(tf.matmul(l2,hidden_3_layer['weights']), hidden_3_layer['biases'])
				l3 = tf.nn.relu(l3)
				output_l = tf.add(tf.matmul(l3,output_layer['weights']) , output_layer['biases'])
				return output_l

			# Model Scores
			self.model_scores = three_layer_network(self.tf_train_dataset)
    
   			# Loss
			self.loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=self.model_scores, labels=self.tf_train_labels))
  
    		# Optimizer.	
			self.optimizer = tf.train.AdamOptimizer().minimize(self.loss)
    
    		# Predictions
			self.train_prediction = tf.nn.softmax(self.model_scores)
			self.test_prediction = tf.nn.softmax(three_layer_network(self.tf_test_dataset))
			print(self.test_prediction)



	def train_network(self):

		num_steps = self.train_labels.shape[0]

		with tf.Session(graph=self.graph) as session:
			tf.global_variables_initializer().run()

			for i in range(0,1):

				self.train_dataset, self.test_dataset, self.train_labels, self.test_labels = train_test_split(
					self.liste_combinaison, self.verite_terrain, test_size = .1, random_state = 12)

				correct = 0

				for step in range(num_steps):
					offset = (step * self.batch_size) % (self.train_labels.shape[0] - self.batch_size)
					minibatch_data = self.train_dataset[offset:(offset + self.batch_size), :]
					minibatch_labels = self.train_labels[offset:(offset +self.batch_size)]

					feed_dict = {self.tf_train_dataset : minibatch_data, self.tf_train_labels : minibatch_labels}

					_, l, predictions = session.run([self.optimizer, self.loss, self.train_prediction], feed_dict = feed_dict)

					if abs(minibatch_labels[0][0]-predictions[0][0])<0.01 and abs(minibatch_labels[0][1]-predictions[0][1])<0.01 \
					and abs(minibatch_labels[0][2]-predictions[0][2])<0.01:
						correct+=1

				accuracy = float(correct)/float(self.train_labels.shape[0])
				print("accurancy : ",round(accuracy*100,2)," %")



	def predict_result(self,dat):

		with tf.Session(graph=self.graph) as session:
			tf.global_variables_initializer().run()
			feed_dict = {self.tf_train_dataset : dat, self.tf_train_labels : np.array([[0,0,0]])}
			_, ls, predic = session.run([self.optimizer, self.loss, self.train_prediction],feed_dict=feed_dict)
     		return predic












