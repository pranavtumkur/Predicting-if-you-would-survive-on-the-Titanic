# Predicting if you would survive on the Titanic

<p align="center">
  <img src="https://user-images.githubusercontent.com/65482013/115981795-1f22c200-a5b4-11eb-9193-6243812e53ba.jpg" />
</p>

Following are the steps, this project follows-

1. Importing [Titanic dataset](https://www.kaggle.com/c/titanic) from [Kaggle](https://www.kaggle.com/)
2. Perfoming EDA and forming inferences via the peculiar trends via a [Jupyter Notebook](https://github.com/pranavtumkur/Predicting-if-you-would-survive-on-the-Titanic/blob/main/EDA%20and%20ML%20model%20of%20Titanic%20survival.ipynb)
3. Training, testing and optimizing a ML Logistic Regression model
4. Pickling this [ML model](https://github.com/pranavtumkur/Predicting-if-you-would-survive-on-the-Titanic/blob/main/model.pkl)
5. Creating an [index.html](https://github.com/pranavtumkur/Predicting-if-you-would-survive-on-the-Titanic/blob/main/templates/index.html) file to capture user inputs and send it to Python
6. Building a Flask API(https://github.com/pranavtumkur/Predicting-if-you-would-survive-on-the-Titanic/blob/main/app.py)-
    1. To deploy the index.html created to a generic web address
    2. To receive user entered data into Python
    3. To send predicted value (using the pickled ML Model) back to the [web address](http://127.0.0.1:5000/)
7. Deploying the Flask API to my [Heroku app](https://predicting-survival-on-titanic.herokuapp.com/) so it can be used by anyone and everyone 


