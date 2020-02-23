
# Module 1 Final Project

## Data and Objective

For this project, we will be working with the King County House Sales dataset. The dataset can be found in the file `"kc_house_data.csv"`, in this repo.

The description of the column names can be found in the column_names.md file in this repository.

We answer 3 questions in this project. 1) Using multivariate ridge regression to predict house prices. 2) Based on your house condition and zipcode what is the best time to sell? 3) Recommend a list of houses based on parameters you choose.



## Files
This project has two notebooks. One is the student.ipynb which has all the analysis and the content of the project in it. The second is the Auxillary.ipynb which has helper functions. The following are the helper functions in Auxillary.ipynb and their functions

### Auxillary.ipynb
withnfeatures() - Creates a ridge regression model starting from the most important feature according to the correlation matrix and adding less important features as we go along. Helpful for visualization of importance of features

cattonum_lin() converting categorical data into numerical one and "linearizing" it, i.e. label encoding the categorical labels so that the data falls on a straight line

fix_skewed() log transforms skewed data for regression

plot_corr() plots a correlation matrix of given columns


### Images Folder
Used for storing images created during analysis

### presentation.pdf
PDF of non-technical presentation

### Blog
https://aghalsasi-datascience.blogspot.com/2020/01/king-county-housing-beginner-analysis.html