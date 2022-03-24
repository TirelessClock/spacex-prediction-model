# SpaceX Prediction Model

## Introduction
SpaceX has had over a hundred and fifty rocket launches over its 20 years of existence. The success or failure of these launches have been dependent on several factors including, though not limited to, the Payload Mass of the rocket, Booster Version, Destination Orbit etc. 
In this project, I have used this data, collected from the SpaceX public API, to train a Logistic Regression Model to predict the success or failure of a future flight. 


## The project

1. `dataCleanMain.py`: Collected data information from the SpaceX official API (https://api.spacexdata.com/v4/launches/past)  of previous launches using the Python Request library. This file further contains the data wrangling process using the Pandas Library. The obtained data was stored in .CSV files `dataset.csv` and `dataset2.csv`.
2. `dataCleanHelper.py`: Wrote the functions used in dataCleanMain.py for the cleaning process. These included:
    a. Removal of duplicates and extra information using Pandas.
    b. Making specific API requests for dataframe construction and organisation.
    c. Removing discrepencies in data and file formats as well as syntactical problems. 
    d. Organisation and Binary Classification of "Outcomes" Column of DataFrame for Model Training. 
    e. Function for One Hot Encoding of Columns. 
    f. Removing NULL values and replacing with the mean. 
3. `graphConstructor.py`: Used seaborn and matplotlib libraries to construct appropriate graphs in order to detect inconsistencies. 
4. `MLmodel.py`: Build Logistic Regression model using sklearn and GridSearchCV libraries to predict the outcome of launches (0 for failed launch and 1 for successful launch). 

## Outcome:

Logistic Regression model built using 


## Side Notes:

(Don't bother reading this, I'm writing it for myself)
Over the course of this project, I learnt a LOT about a LOT. This project was pretty significant for several reasons:

1. First proper project of mine.
2. Through this project I learnt how to use Git and Github - concepts I was previously largely unfamiliar with. In fact, this repo isn't the first repo for this project made - over the course of development, I made two successive repositories before this, but deleted them both for a plethora of reasons.
3. Learnt how to use self made modules and packages. Never did that before, and my first try with it was absolutely disastrous (Deleted the second repository because of the horrendous file structuring.)
4. Finally came to use and appreciate file formatting systems, and their immense timesaving potential. 
5. Using this project as an excuse, finally structured my laptop's rat-hair organisation system.
6. Graphs plotting. Another check on my Software Skills Bingo.
