# Zillow Regression Project
by Jeremy Lagunas 07/27/2022

## Project Outline
This project will follow the Data Science Pipeline. All steps of of this pipeline will be documented for review and implementation. The planning phase will be documented on this README. Other steps will be documented on a working notebook, the final report, or their own deliverable as necessary. The process will take place as follows:
1. Plan
2. Acquire
3. Prepare
4. Explore
5. Model
6. Deliver

## Plan

### Project Description
I will be working with the zillow dataset and set out to make a model which accurately predicts home price, A.K.A. the 'zestimate'.

### Inital Questions
1. Are bedrooms more correlated with home price than square feet is?
2. Is there a linear relationship between square feet and price?
3. Ist there a linear relationship between bedrooms and price?

### Null Hypothesis
- The number of bathrooms are not correlated with the home price.

### Alternative Hypothesis
- There is a correlation between the number of bathrooms and home price. 

### Project Goals
- Generate informative visuals to gain a better understanding of the data and how variables interact. 
- Find which features are best to use in a predictive model.
- Create a model which accurately predicts home price within +- 10%.

### Data Dictionary
bed: The number of bedrooms in a house.
bath: The number of bathrooms in a house.
square_feet: The square feet of the house structure.
price: The price of the house. 
lot_square_feet: The square feet of the lot where the house is located.
zipcode: The zipcode in which the house is located.
year_built: The year the house was built. 
pool: How many pools a house has.
fireplace: How many fireplaces a house has. 

## Steps to Reproduce
1. You will need an env.py file which has the host name, username, and password of the mySQL database that contains the zillow database. Store the env file locally in the repo.
2. Clone my repo. Confirm .gitignore is hiding your env file.
3. Import libraries (pandas, matplotlib, seaborn, numpy, sklearn)
4. Run zillow_report
