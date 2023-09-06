# Telecom-Customer-Churn-Prediction

**DOMAIN:** Telecom

**CONTEXT:** A telecom company wants to use their historical customer data and leverage machine learning to predict behaviour in an attempt to retain customers. The end goal is to develop focused customer retention programs.

**DATA  DESCRIPTION:** Each  row  represents  a  customer,  each  column  contains  customer’s  attributes  described  on  the  column  Metadata.  The data set includes information about:
• Customers who left within the last month – the column is called Churn
• Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
• Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
• Demographic info about customers – gender, age range, and if they have partners and dependents.

**PROJECT  OBJECTIVE:** The  objective,  as  a  data  scientist  hired  by  the  telecom  company,  is  to  build  a  model  that  will  help  to  identify  the potential customers who have a higher probability to churn. This will help the company to understand the pain points and patterns of customer churn and will increase the focus on strategizing customer retention.


**DATA EXPLORATION AND DATA CLEANING:**

Combined the two files to create a single file with all the relevant variables and perform the necessary data quality checks and cleaning. In data cleaning, identified the missing values/unexpected values in the dataset and since the number of missing values is very less, dropped the missing value rows. Also, checked if there is any outliers in the dataset. Make sure that the data types of the variables are appropriate as required for our analysis (Here, converted all the categorical variable data types to category and continuous variable data types to int or float).

**DATA ANALYSIS:**

Checked the distribution of data for the continuous (histogram charts) and categorical (pie charts) variables along with the target variable (pie charts). Performed uni-variate, bivariate, and multivariate analysis of the dataset, for example, 5-point summary of the continuous variable, pair plot, correlation matrix plot, and boxplot to detect outliers.


**DATA PREPROCESSING:**

Here, removed the unwanted/irrelevant independent variable/feature based on the above analysis from the dataset. Also, encoded the categorical variable using one-hot encoding and label encoding based on the categories, and scaled the independent variable using standard scaler.


**MODEL BUILDING, EVALUATION AND IMPROVEMENT:**

Used k nearest neighbour, logistic regression, support vector machine (SVM), naive bayes, decision tree, random forest, Ada boost and gradient boost algorithm to predict the churn customer and evaluate the model using confusion metrix, accuracy score, recall score, precision score and f1 score. Further tunned the models using GridsearchCV and compared all the models to find the best model.

**Finalize Ada boost model as the final model and achieved an accuracy of 80.03%.**

**MODEL DEPLOYMENT:**

Created a web app using pickle (used to save and load the model) and streamlit (used o create the web app) to predict the churn customer. (refer to "churn prediction web app.py" file)

