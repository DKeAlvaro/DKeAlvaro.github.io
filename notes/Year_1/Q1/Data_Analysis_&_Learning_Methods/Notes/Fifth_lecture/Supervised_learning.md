# Data Analysis & Learning Methods - Lecture 5

Q: What is supervised learning?
A: It is a type of machine learning where the model learns from data that includes labels or targets. (Page 4)

Q: What is the difference between classification and regression in supervised learning?
A: Classification predicts a categorical label (e.g., 'lemon' or 'orange'), while regression predicts a continuous, real value (e.g., the price of a house). (Page 4)

Q: What is unsupervised learning?
A: It's a type of machine learning that works with data that has no labels, aiming to find patterns like clusters or simpler representations. (Page 4)

Q: Why might a simple heuristic (rule-based) approach fail for complex tasks?
A: Because the variation in data can be enormous, and patterns are often too complex or exist in high-dimensional spaces for humans to define effective rules. (Page 6)

Q: What is the difference between a model-driven and a data-driven approach?
A: A model-driven approach uses a physical understanding of a problem to create a model (e.g., physics), whereas a data-driven approach uses the data itself as the primary source to construct a model (e.g., machine learning). (Page 7)

Q: What are the three components of the expected mean squared error in the bias-variance decomposition?
A: Bias, variance, and irreducible error. (Page 8)

Q: What is the main takeaway from the "garbage in, garbage out" principle in machine learning?
A: The quality and choice of features in your dataset are crucial; machine learning models cannot fix a dataset with uninformative or "crappy" data. (Page 12)

Q: What is a parametric approach in machine learning?
A: It is an approach where the model is defined by a set of trainable parameters $\theta$, commonly written as $f_{\theta}(x)$. (Page 13)

Q: How does the K-Nearest Neighbours (KNN) algorithm classify a new data point?
A: It looks at the 'k' closest data points (neighbours) in the training set and assigns the new point the majority class of those neighbours. (Page 15)

Q: Why is KNN considered a "memory-based" or "non-parametric" method?
A: Because it does not learn an explicit model with parameters; instead, it stores all training instances in memory to make predictions. (Page 16)

Q: What is a hyperparameter?
A: A hyperparameter is a configuration parameter that is set before the training process begins and is not learned from the data (e.g., the value of 'k' in KNN). (Page 17)

Q: What is the effect of increasing the value of 'k' in KNN?
A: Increasing 'k' generally leads to a smoother decision boundary, which makes the model more robust to noise but potentially less able to capture local patterns. (Page 18)

Q: What is the mathematical formula for a simple linear classifier?
A: The classifier calculates a score using the function $f(x, w) = wx + b$. (Page 20)

Q: In logistic regression, what function is used to map the linear output score to a probability between 0 and 1?
A: The logistic function, also known as the sigmoid function: $\sigma(z) = \frac{1}{1 + e^{-z}}$. (Page 22)

Q: What is the binary cross-entropy loss function used for?
A: It measures the error in a binary classification model, penalizing it for making wrong predictions with high confidence. (Page 22)

Q: What defines the decision boundary in a logistic regression classifier?
A: The decision boundary is the line or hyperplane where the input to the sigmoid function is zero ($w^{*}x + b = 0$), corresponding to a predicted probability of 0.5. (Page 23)

Q: For multi-class classification, what function generalizes the sigmoid and what does it do?
A: The softmax function. It takes a vector of raw scores (logits) and transforms them into a probability distribution where all values are between 0 and 1 and sum to 1. (Page 24)

Q: What are the three main types of nodes in a decision tree?
A: The root node (the starting point), internal (split) nodes (where decisions are made), and terminal (leaf) nodes (the final predictions). (Page 29)

Q: What is randomized node optimization in the context of training decision trees?
A: It is a technique where, for each node, a random subset of possible split parameters is evaluated, and the best one is chosen, rather than searching through all possibilities. (Page 34)

Q: What is Information Gain and how is it used in decision trees?
A: Information Gain is a metric used to choose the best split at a node. It measures the reduction in entropy (or increase in purity) achieved by splitting the data. The split with the highest information gain is chosen. (Page 35)

Q: What is the formula for Shannon's entropy?
A: The entropy of a set $S$ is calculated as $H(S) = -\sum_{c \in \mathcal{C}} p_c \log p_c$, where $p_c$ is the fraction of items in class $c$. (Page 35)

Q: What are the common stopping criteria for growing a decision tree?
A: The process stops when a branch reaches a predefined maximum depth, a total node limit is reached, or a node contains samples from only one class. (Page 44)

Q: What are two pros and two cons of decision trees?
A: Pros: They are easy to interpret and fast. Cons: They have relatively low predictive power and high variance (tendency to overfit). (Page 51)

Q: What is the core idea behind a Random Forest?
A: A Random Forest combines a large number of diverse, "weak" decision trees into a single, "strong" learner to improve predictive accuracy and control overfitting. (Page 54)

Q: What are the two primary methods for introducing randomness into a Random Forest?
A: Bagging (training each tree on a random subset of data) and Randomized Node Optimization (considering only a random subset of features/splits at each node). (Page 55)

Q: How does a Random Forest make a final prediction for classification?
A: It averages the probabilistic predictions from all individual trees in the forest. (Page 59)

Q: In a Random Forest, what is the effect of increasing tree depth (D) and decreasing the randomness parameter ($\rho$)?
A: Increasing depth allows for more complex models that can overfit. Decreasing $\rho$ increases randomness, making trees more diverse, which typically reduces overfitting and creates smoother decision boundaries. (Pages 61, 63)

Q: Why is it beneficial for a model's prediction confidence to correlate with its accuracy?
A: It makes the model's output more reliable. High-confidence predictions can be trusted more, while low-confidence ones can be flagged for human review. (Page 67)

Overview: Fifth lecture

Date: 19 Sep 2025