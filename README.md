# SpaceX Prediction Model

## Introduction
SpaceX has had over a hundred and fifty rocket launches over its 20 years of existence. The success or failure of these launches have been dependent on several factors including, though not limited to, the Payload Mass of the rocket, Booster Version, Destination Orbit etc. 
In this project, I have used this data, collected from the SpaceX public API, to train a Logistic Regression Model to predict the success or failure of a future flight. 


## Project Details

- `dataCleanMain.py`: Collected data information from the SpaceX official API (https://api.spacexdata.com/v4/launches/past)  of previous launches using the Python Request library. This file further contains the data wrangling process using the Pandas Library. The obtained data was stored in .CSV files `dataset.csv` and `dataset2.csv`.
- `dataCleanHelper.py`: Wrote the functions used in dataCleanMain.py for the cleaning process. These included:
    a. Removal of duplicates and extra information using **Pandas**.
    b. Making specific API requests for dataframe construction and organisation.
    c. Removing discrepencies in data and file formats as well as syntactical problems. 
    d. Organisation and Binary Classification of "Outcomes" Column of DataFrame for Model Training. 
    e. Function for One Hot Encoding of Columns. 
    f. Removing NULL values and replacing with the mean. 
- `graphConstructor.py`: Used **seaborn** and **matplotlib** libraries to construct appropriate graphs in order to detect inconsistencies. 
- `MLmodel.py`: Built Logistic Regression model using **sklearn** and **GridSearchCV** libraries to predict the outcome of launches (0 for failed launch and 1 for successful launch). 
- `dataset.csv`: In the process of dataframe construction, I had to load 150 individual data pieces from different SpaceX APIs, a process that involved frequent requests and back and forth from servers, and took over 9 minutes to complete. This .CSV was made to store that data locally and hence save myself time.
- `dataset2.csv`: The final dataset that was to be used to train and test the ML model. This dataset contained all numeric data (**float64**) and replaced Categorical Datatypes with One Hot Encoding. 

## Outcome:

Logistic Regression model built using sklearn and GridSearchCV on a data of size 154 returned the following result:

Tuned Hyperparameters: {'C':0.1, 'penalty': 'l1', 'solver saga'}

Accuracy: 0.8846

## Side Notes:

- When dealing with NaN values in the table, I had two choices, both with its demerits - replacing the NaN values with the mean and removing the entire rows containing NaN values. Going with the former resulted in a relatively innacurate dataset, while going with the latter resulted in a much smaller dataset. I picked what I deemed to be the lesser of two evils, and went with the mean option. 
- The relatively low accuracy is a result of a small size (154 rows) of dataset and corresponding large number of parameters (11 columns). 
- This final project was the third draft of my project. Two previous drafts were made and deleted - one because of issues connecting with GitHub (This was my first time building a project synchronously with GitHub, and hence had difficulties in the syncing setup), and the other because of a messy file structure I employed while learning and implementing file structuring and modules
