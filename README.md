# fake-news-detection-
This is a project for fake news detection and contains the website's code. This machine-learning project determines whether a news article is fake or real. I have created the machine learning model on the jupyter notebook, and the website has been created using anvil uplink, an online cloud-based service. The machine learning models used in the project are -

The methodologies used are Classification and regression. 

The Classification algorithm is a Supervised Learning technique used to identify the category of new observations based on training data. In Classification, a program learns from the given dataset or observations and classifies new observations into several classes or groups. Such as, Yes or No, 0 or 1, Spam or Not Spam, in this case - fake or real. Classes can be called targets/labels or categories.

Regression is a supervised learning technique that helps find the correlation between variables and enables us to predict the continuous output variable based on one or more predictor variables. It is mainly used for prediction, in this case, indicating whether the news is fake or real. 

Logistic Regression: Logistic regression is another supervised learning algorithm which is used to solve classification problems.

Random Forest Classifier: Random Forest is a classifier that contains several decision trees on various subsets of the given dataset and takes the average to improve the predictive accuracy of that dataset.

TensorFlow: Tensor flow is an open-source software library. TensorFlow is a software library for numerical computation using data flow graphs.

Datasets - 
The dimensions for the true dataset are - (21417, 5)
The dimensions for the false dataset are -(23481, 4)
The dimensions for the news dataset are - (7796,3)
Total data points -  248,163

Attributes for True.csv dataset - the title of the news , the text of the news and the subject of the news.
Attributes for Fake.csv dataset - title of the news,text of the news and the subject of the news.
Attributes of news.csv dataset - the title of the news , the text of the news and the label of the news.

Website - 
The website of the project has been made using an anvil uplink server. You can watch online tutorials explaining how to deploy jupyter notebook to the Anvil uplink server. There are different buttons and text; you can design a webpage quite quickly compared to using HTML or CSS. I have uploaded the code used in the Anvil server to create the website and uploaded the code on the jupyter notebook. The output on the website is only through logistic regression and random forest classifier. The tensor flow jupyter notebook has yet to be deployed on the website.
