# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# #  EPA-122A *Spatial* Data Science
#
#
# ## Homework 5: Plotting, Simple Linear Regression, K-NN Regression
#
# **TU Delft**<br>
# **Q2 2024**<br>
# **Instructors:** Giacomo Marangoni, Theodoros Chatzivasileiadis <br>
# ---
#

# %% [markdown]
# ## Exercise 1
#
# Do the following:
# * Make a figure with the logistic function, hyperbolic tangent, and rectified linear unit. (see thelab for reference on what these are)
# * Use different line styles for each plot
# * Put a legend on your figure
#
# Here's an example of a figure:
# ![](figs/nice_plots.png)

# %% [markdown]
# your code here
# don't forget to import the libraries you need


# %% [markdown]
# %load hw-solutions/exercise1.py


# %% [markdown]
# ## Exercise 2
#
# These figures look nice in the plot and it makes sense for comparison. Now let's put the 3 different figures in separate plots.
#
# * Make a separate plot for each figure and line them up on the same row.

# %% [markdown]
# your code here


# %% [markdown]
# %load hw-solutions/exercise2.py


# %% [markdown]
# ## Exercise 3
#
# * Make a grid of 2 x 3 separate plots, 3 will be empty. Just plot the functions and do not worry about cosmetics. We just want you ro see the functionality.

# %% [markdown]
# your code here


# %% [markdown]
# %load hw-solutions/exercise3.py


# %% [markdown]
# ## Exercise 4

# %% [markdown]
# * Make two numpy arrays, called x_train and y_train, out of this data: x = [1, 2, 3], y = [2, 2, 4]
# * Check the dimentions of these arrays
# * Try to reshape them into a different shape (2D arrays)
# * Make points into a very simple scatterplot
# * Make a better scatterplot (always remember our plots commandments)

# %% [markdown]
# your code here


# %% [markdown]
# %load hw-solutions/exercise4.py


# %% [markdown]
# ## Exercise 5: Simple linear regression with automobile data
#
# We will now use `sklearn` to predict automobile mileage per gallon (mpg) and evaluate these predictions.

# %% [markdown]
# We need to choose the variables that we think will be good predictors for the dependent variable `mpg`.

# %% [markdown]
# <div class="exercise"><b>Exercise 5.1</b></div>
#
# * Load the data `mtcars` and split them into a training set and a test set.
# * Pick one variable to use as a predictor for simple linear regression. Discuss your reasons with a friend or group member if you like.
# * Use markdown to justify your choice with some visualisations.
# * Is there a second variable you'd like to use? For example, we're not doing multiple linear regression here, but if we were, is there another variable you'd like to include if we were using two predictors?

# %% [markdown]
# **IMPORTANT:** Remember that your response variable `y_train` can be a vector but your predictor variable `x_train` ***MUST*** be an array!

# %% [markdown]
# %load hw-solutions/exercise5.1.py


# %% [markdown]
# <div class="exercise"><b>Exercise 5.2</b></div>
#
# For data used in exercise 4.1,
#
# * Use `sklearn` to fit the training data using simple linear regression.
# * Use the model to make mpg predictions on the test set.
# * Plot the data and the prediction.
# * Print out the mean squared error for the training set and the test set and compare.

# %% [markdown]
# %load hw-solutions/exercise5.2.py
