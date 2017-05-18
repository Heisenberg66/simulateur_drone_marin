import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split


num_observations = 1000

# liste de toutes les possibilites du sonar

liste = np.array([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9])


    
for i in range(0,10):
	liste1 = np.array([0,0,0,0,0,0,0,0,0,0])
	liste1[i] = 1

	for j in range(0,10):
		liste2 = np.array([0,0,0,0,0,0,0,0,0,0])
		liste2[j] = 1

		for z in range(0,10):
			liste3 = np.array([0,0,0,0,0,0,0,0,0,0])
			liste3[z]=1
			liste_final =np.concatenate((liste1,liste2,liste3), axis=0)
			liste = np.vstack(( liste,liste_final )).astype(np.float32)

liste = np.delete(liste, 0, axis=0)


# ---------------------------------------------------------------------------------------------------------------------------

# toute les sortie possible 

simulated_labels = np.hstack((np.zeros(500),
				np.ones(500)))

# ----------------------------------------------------------------------------------------------------------------------------



labels_onehot = np.zeros((simulated_labels.shape[0], 10)).astype(int)
labels_onehot[np.arange(len(simulated_labels)), simulated_labels.astype(int)] = 1

#----------------------------------------------------------------------------------------------------------------------------

# definition pourcentage de datas train et test , ici test size = .1 ==> 900 rows train, 100 rows test

train_dataset, test_dataset, train_labels, test_labels = train_test_split(
     liste, labels_onehot, test_size = .1, random_state = 12)

# --------------------------------------------------------------------------------------------------------------------------

# init layer neural network

hidden_nodes = 50 # nb nerons per layers
num_labels = train_labels.shape[1] 
batch_size = 1
num_features = train_dataset.shape[1]
learning_rate = .01

graph = tf.Graph()
with graph.as_default():
    
    # Data
    tf_train_dataset = tf.placeholder(tf.float32, shape = [None, num_features])
    tf_train_labels = tf.placeholder(tf.float32, shape = [None, num_labels])
    tf_test_dataset = tf.constant(test_dataset)
  
    # Weights and Biases
    layer1_weights = tf.Variable(tf.truncated_normal([num_features, hidden_nodes]))
    layer1_biases = tf.Variable(tf.zeros([hidden_nodes]))
    
    layer2_weights = tf.Variable(tf.truncated_normal([hidden_nodes, num_labels]))
    layer2_biases = tf.Variable(tf.zeros([num_labels]))
    
    # Three-Layer Network
    def three_layer_network(data):
        input_layer = tf.matmul(data, layer1_weights)
        hidden = tf.nn.relu(input_layer + layer1_biases)
        output_layer = tf.matmul(hidden, layer2_weights) + layer2_biases
        return output_layer
    
    # Model Scores
    model_scores = three_layer_network(tf_train_dataset)
    
    # Loss
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=model_scores, labels=tf_train_labels))
  
    # Optimizer.
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
    
    # Predictions
    train_prediction = tf.nn.softmax(model_scores)
    test_prediction = tf.nn.softmax(three_layer_network(tf_test_dataset))


def accuracy(predictions, labels):
    preds_correct_boolean =  np.argmax(predictions, 1) == np.argmax(labels, 1)
    correct_predictions = np.sum(preds_correct_boolean)
    accuracy = 100.0 * correct_predictions / predictions.shape[0]
    return accuracy

# -------------------------------------------------------------------------------------------------------------------------------------------


num_steps = 1001

with tf.Session(graph=graph) as session:
    tf.initialize_all_variables().run()

    for step in range(num_steps):
        offset = (step * batch_size) % (train_labels.shape[0] - batch_size)
        minibatch_data = train_dataset[offset:(offset + batch_size), :]
        minibatch_labels = train_labels[offset:(offset + batch_size)]

        feed_dict = {tf_train_dataset : minibatch_data, tf_train_labels : minibatch_labels}
        
        _, l, predictions = session.run(
            [optimizer, loss, train_prediction], feed_dict = feed_dict
            )
        

        if step % 100 == 0:
            print ("Minibatch loss at step ",step," : ",l)
    print ('Test accuracy:',format(accuracy(test_prediction.eval(), test_labels)),' %')


