# Data-Driven-Decision-Support-for-Aircraft-Procurement
## Project Summary
This project  leverages the Pandas package to:
1) Import a .csv dataset data to a Jupyter Notebook.
2) Perform Extract Transform Load <strong> ETL </strong> processes by applying lambda functions to perform data transformations (drop entries with unknown values, eliminate duplicates, convert data types, and data aggregation).
3) Perform descriptive statistics on (float and int) variables to determine the appropriate measure of central tendency to impute for missing values.
4) Applying the <strong>.groupby() </strong> method to create subgroups of a DataFrame suitable for analyzing and visualizing the relationship between specific aircraft makes and models and their potential correlation to fatality or survival rates in the event of accidents/ incidents.
The analysis yields three recommendations on the aircraft models the company should procure and operate after entering the commercial aviation industry.
## Data Understanding
This project aims to support the company's data-driven decisions to procure relatively low-risk airplane models to operate the fleet in the commercial and private enterprise sectors. It analyzes a dataset compiled by the National Transportation Safety board and retrieved from <html>https://doi.org/10.34740/KAGGLE/DSV/4875576</html>. Recommendations on the safest, practical, and logistically viable aircraft (model and make) for various aviation services the company can venture into to diversify its portfolio are backed up by descriptive statistics and justified by interactive visualizations created using Tableau Public. 

<strong> Features: </strong> Prior to data cleaning, the original dataset comprises 31 columns and 88889 rows. The columns are meticulously organized to capture variables of interest in aircraft accidents and incidents. Extracting, analyzing, and visualizing relevant data from the dataset is vital to shedding insight into the safest, low-risk airplane models for a new entrant to the commercial aviation industry.

<strong> Target: </strong> For this project, the target variables categorize into Dimensions and Measures. The Dimension variables include: `Event.Date`, `Investigation.Type`, `Aircraft.Damage`, `Location`, `Make`, `Model`, `Number.of.Engine`, 'Engine.Type` `Weather.Condition`, and `Purpose.of.flight`. The Measure variables include: `Total.Fatal.Injuries`, `Total.Serious.Injuries`, `Total.Minor.Injuries`, and `Total.Uninjured`. The other columns are deemed inapplicable for this project and dropped prior to data cleaning processes. 

## Problem Statement





## Business Objectives
1. <strong> Goal: </strong> To design a program to 




2. <strong> Specific Objectives: </strong>



## Requirements to Meet Objectives
1. <strong> Load the Data </strong>
* Load a .csv dataset, create the working `df` and inspect imported data.
2. <strong> Perform Extract Transform Load (ETL) processes </strong>
* Apply lambda functions to perform data transformations (drop entries with unknown values, eliminate duplicates, convert data types, and data aggregation).
3. <strong> Imputing missing values </strong>
* Perform descriptive statistics on (float and int) variables to determine the appropriate measure of central tendency to impute for missing values.
4. <strong> Analyzing the cleaned dataset </strong>
* Applying the <strong>.groupby() </strong> method to create subgroups of a DataFrame suitable for analyzing and visualizing the relationship between specific aircraft makes and models and their potential correlation to fatality or survival rates in the event of accidents/ incidents.
5. <strong> Deducing recommendations based on data analysis findings </strong>
* The grand aim for the project is met by recommending the safest aircraft the company should procure based on respective applicability, and operational feasibility for specific aviation services the business will be offering upon entry to the industry. 


