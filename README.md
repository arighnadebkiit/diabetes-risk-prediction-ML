# diabetes-risk-prediction-using-machine-learning
This repository contains machine learning models to predict risk of having diabetes at an early stage. 

The dataset is located in the folder name Dataset. The data of 520 persons were collected from the Sylhet Diabetes Hospital, Sylhet, Bangladesh and were approved by the medical practitioner. The dataset is owned by M. M. Faniqul Islam, Rahatara Ferdousi, Sadikur Rahman, and Humayra Yasmin Bushra.

In this work, the following machine learning models are applied on the diabetes risk prediction dataset:
1. Logistic regression
2. K-nearest neighbors with number of neighbors = 5 and 10
3. Random forest with number of trees = 10, 20 and 100
4. Decision tree
5. Support vector machine with kernel type: radial basis function, linear, sigmoid and polynomial of degree 4
6. Naive Bayes with classifier type: Gaussian, Bernoulli, Categorical and Multinomial.

The dataset is also split into following training and test set size:
1. 80:20 (80% training and 20% test set)
2. 75:25 (75% training and 25% test set)
3. 70:30 (70% training and 30% test set)
4. 65:35 (65% training and 35% test set)

To evaluate the performance of the machine learning models, following metrics are considered:
1. Test accuracy
2. Confusion matrix
3. Precision, recall, F1-score
4. Area under the receiver operating characteristics (AUROC)
5. Mean validation accuracy and standard deviation

For detailed results and discussion, see the result.pdf
