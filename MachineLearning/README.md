
There are so many algorithms that it can feel overwhelming when algorithm names are thrown around and you are expected to just know what they are and where they fit.

To overcome this, I would like to categorize the algorithms in two ways as follows:
* Algorithms Grouped by Learning Style.
* Algorithms Grouped by Similarity.

# Algorithms Grouped by Learning Style

There are different ways an algorithm can model a problem based on its interaction with the world (or) environment (or) whatever we want to call the input data.

This taxonomy (or) way of organizing machine learning algorithms is useful because it forces you to think about the roles of the input data and the model preparation process and select one that is the most appropriate for your problem in order to get the good result.

### 1. Supervised Learning

The Input data is called Training data and has a known label or result such as spam/not-spam or a stock price at a given time.

A model is prepared through a training process in which it is required to make predictions and is corrected when those predictions are wrong. The training process continues until the model achieves a desired level of accuracy on the training data.

<u>Example problems</u> include Classification and Regression.

<u>Example Algorithms include</u> : Logistic Regression and Back Propagation in Neural Networks.

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Supervised-Learning-Algorithms.png" />
</p>

### 2. Unsupervised Learning

Input data is NOT labeled and does not have a known result.

A model is prepared by deducing structures present in the input data. This may be to extract general rules. It may be through a mathematical process to systematically reduce redundancy, or it may be to organize data by similarity.

<u>Example problems</u> are clustering, dimensionality reduction and association rule learning.

<u>Example algorithms include</u> : the Apriori algorithm and K-Means.

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Unsupervised-Learning-Algorithms.png" />
</p>

### 3. Semi-Supervised Learning

Input data is a mixture of labeled and unlabelled examples.

There is a desired prediction problem but the model must learn the structures to organize the data as well as make predictions.

<u>Example problems</u> are classification and regression.

<u>Example algorithms</u> are extensions to other flexible methods that make assumptions about how to model the unlabeled data.

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Semi-supervised-Learning-Algorithms.png" />
</p>



# Algorithms Grouped By Similarity

Algorithms are often grouped by similarity in terms of their function (how they work). 

This is a useful grouping method, but it is not perfect. There are still algorithms that could just as easily fit into multiple categories like Learning Vector Quantization that is both a neural network inspired method and an instance-based method. There are also categories that have the same name that describe the problem and the class of algorithm such as Regression and Clustering.

### 1. Regression Algorithms

Regression is concerned with modeling the relationship between variables that is iteratively refined using a measure of error in the predictions made by the model.

Regression methods are a workhorse of statistics and have been co-opted into statistical machine learning. This may be confusing because we can use regression to refer to the class of problem and the class of algorithm. In essence, Regression is a process.

The most popular regression algorithms are:

* Ordinary Least Squares Regression (OLSR)
* Linear Regression
* Logistic Regression
* Stepwise Regression
* Multivariate Adaptive Regression Splines (MARS)
* Locally Estimated Scatterplot Smoothing (LOESS)

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Regression-Algorithms.png" />
</p>

### 2. Instance-based Algorithms

Instance-based learning model is a Decision problem with instances or examples of training data that are deemed important or required to the model.

Such methods typically build up a database of example data and compare new data to the database using a similarity measure in order to find the best match and make a prediction. For this reason, instance-based methods are also called <u>winner-take-all</u> methods and <u>memory-based learning</u>. Focus is put on the representation of the stored instances and similarity measures used between instances.

The most popular instance-based algorithms are:

* k-Nearest Neighbor (kNN)
* Learning Vector Quantization (LVQ)
* Self-Organizing Map (SOM)
* Locally Weighted Learning (LWL)
* Support Vector Machines (SVM)

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Instance-based-Algorithms.png" />
</p>

### 3. Regularization Algorithms

An extension made to another method (typically regression methods) that penalizes models based on their complexity, favoring simpler models that are also better at generalizing.

I have listed regularization algorithms separately here because they are popular, powerful and generally simple modifications made to other methods.

The most popular regularization algorithms are:

* Ridge Regression
* Least Absolute Shrinkage and Selection Operator (LASSO)
* Elastic Net
* Least-Angle Regression (LARS)    

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Regularization-Algorithms.png" />
</p>

### 4. Decision Tree Algorithms

Decision tree methods construct a model of decisions made based on actual values of attributes in the data.

Decisions fork in tree structures until a prediction decision is made for a given record. Decision trees are trained on data for classification and regression problems. Decision trees are often fast and accurate and a big favorite in machine learning.

The most popular decision tree algorithms are:

* Classification and Regression Tree (CART)
* Iterative Dichotomiser 3 (ID3)
* C4.5 and C5.0 (different versions of a powerful approach)
* Chi-squared Automatic Interaction Detection (CHAID)
* Decision Stump
* M5
* Conditional Decision Trees

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Decision-Tree-Algorithms.png" />
</p>

### 5. Bayesian Algorithms

Bayesian methods are those that explicitly apply Bayes’ Theorem for problems such as classification and regression.

The most popular Bayesian algorithms are:

* Naive Bayes
* Gaussian Naive Bayes
* Multinomial Naive Bayes
* Averaged One-Dependence Estimators (AODE)
* Bayesian Belief Network (BBN)
* Bayesian Network (BN)

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Bayesian-Algorithms.png" />
</p>

### 6. Clustering Algorithms

Clustering, like regression, describes the class of problem and the class of methods.

Clustering methods are typically organized by the modeling approaches such as centroid-based and hierarchal. All methods are concerned with using the inherent structures in the data to best organize the data into groups of maximum commonality.

The most popular clustering algorithms are:

* k-Means
* k-Medians
* Expectation Maximisation (EM)
* Hierarchical Clustering

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Clustering-Algorithms.png" />
</p>

### 7. Association Rule Learning Algorithms

Association rule learning methods extract rules that best explain observed relationships between variables in data.

These rules can discover important and commercially useful associations in large multidimensional datasets that can be exploited by an organization.

The most popular association rule learning algorithms are:

* Apriori algorithm
* Eclat algorithm

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Assoication-Rule-Learning-Algorithms.png" />
</p>

### 8. Artificial Neural Network Algorithms

Artificial Neural Networks are models that are inspired by the structure and/or function of biological neural networks.

They are a class of pattern matching that are commonly used for regression and classification problems but are really an enormous subfield comprised of hundreds of algorithms and variations for all manner of problem types.

Note that I have separated out Deep Learning from neural networks because of the massive growth and popularity in the field. Here we are concerned with the more classical methods.

The most popular artificial neural network algorithms are:

* Perceptron
* Multilayer Perceptrons (MLP)
* Back-Propagation
* Stochastic Gradient Descent
* Hopfield Network
* Radial Basis Function Network (RBFN)

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Artificial-Neural-Network-Algorithms.png" />
</p>

### 9. Deep Learning Algorithms

Deep Learning methods are a modern update to Artificial Neural Networks that exploit abundant cheap computation.

They are concerned with building much larger and more complex neural networks and, as commented on above, many methods are concerned with very large datasets of labelled analog data, such as image, text. audio, and video.

The most popular deep learning algorithms are:

* Convolutional Neural Network (CNN)
* Recurrent Neural Networks (RNNs)
* Long Short-Term Memory Networks (LSTMs)
* Stacked Auto-Encoders
* Deep Boltzmann Machine (DBM)
* Deep Belief Networks (DBN)

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Deep-Learning-Algorithms.png" />
</p>

### 10. Dimensionality Reduction Algorithms

Like clustering methods, dimensionality reduction seek and exploit the inherent structure in the data, but in this case in an unsupervised manner or order to summarize or describe data using less information.

This can be useful to visualize dimensional data or to simplify data which can then be used in a supervised learning method. Many of these methods can be adapted for use in classification and regression.

* Principal Component Analysis (PCA)
* Principal Component Regression (PCR)
* Partial Least Squares Regression (PLSR)
* Sammon Mapping
* Multidimensional Scaling (MDS)
* Projection Pursuit
* Linear Discriminant Analysis (LDA)
* Mixture Discriminant Analysis (MDA)
* Quadratic Discriminant Analysis (QDA)
* Flexible Discriminant Analysis (FDA)

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Dimensional-Reduction-Algorithms.png" />
</p>

### 11. Ensemble Algorithms

Ensemble methods are models composed of multiple weaker models that are independently trained and whose predictions are combined in some way to make the overall prediction.

Much effort is put into what types of weak learners to combine and the ways in which to combine them. This is a very powerful class of techniques and as such is very popular.

* Boosting
* Bootstrapped Aggregation (Bagging)
* AdaBoost
* Weighted Average (Blending)
* Stacked Generalization (Stacking)
* Gradient Boosting Machines (GBM)
* Gradient Boosted Regression Trees (GBRT)
* Random Forest

<p align="center">
  <img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/Ensemble-Algorithms.png" />
</p>

***

## Other Lists of Machine Learning Algorithms
There are other great lists of algorithms out there if you’re interested. Below are few hand selected examples.

* [List of Machine Learning Algorithms](https://en.wikipedia.org/wiki/Outline_of_machine_learning#Machine_learning_algorithms) : On Wikipedia. Although extensive, I do not find this list or the organization of the algorithms particularly useful.
* [Machine Learning Algorithms Category](https://en.wikipedia.org/wiki/Category:Machine_learning_algorithms): Also on Wikipedia, slightly more useful than Wikipedias great list above. It organizes algorithms alphabetically.
* How to Learn Any Machine Learning Algorithm:  [Useful Link ](https://machinelearningmastery.com/how-to-learn-a-machine-learning-algorithm/)
