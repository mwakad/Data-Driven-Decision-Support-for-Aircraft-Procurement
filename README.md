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
Operating airplanes for commercial and private enterprises is a potentially profitable portfolio diversification strategy for the company. However, venturing into such a highly sensitive sector necessitates data-driven decisions, strategic implementation, and formative performance evaluation. Thankfully, digital maturity in leveraging novel data analytics is a key driver for aircraft safety. The insights yielded by this project have a significant impact in supporting the company's data-driven decisions in procuring a safe aircraft fleet to operate in a highly sensitive sector.



## Business Objectives
1. <strong> Goal: </strong> To design a program for helping the stakeholders of a company aiming to diversify its portfolio by purchasing and operating a fleet of airplanes with a high safety rating for commercial and private enterprises to make data-driven procurement decisions.

2. <strong> Specific Objectives: </strong>
* To indentify the least safe aircraft the company should refrain from purchasing.
* To identify the relatively safer single-engine, and multi-engine aircraft the company can consider purchasing.
* To recommend the safest and most operationally feasible aircraft models the company should procure to operate in specific applications (`Purpose.of.flight`).



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


## Objective 1
### Least Safe Aircraft Models  
* The .`groupby()` method is used to group the cleaned DataFrame (`df_clean`) by `Make` (the manufacturer) and `Model` (a specific aircraft model).
* Hence, each unique combination of an aircraft’s Make and Model is treated as a single group to avoid ambiguity since aircraft models made by different manufacturers can share the exact model name or a similar str-num identifier.
* Additionally, grouping an aircraft’s `Make` and `Model` optimizes the readability of plotted visualizations.
* The aggregate sum of fatalities `Total.Fatal.Injuries` for each `Make` and `Model` are sorted in descending order (ascending = False) and filtered (head = 10) to select the top-10 least safe aircraft in terms of respectively attributed fatalities.
* A horizontal barplot is plotted using Seaborn to visualize the top 10 aircraft the company should not purchase.

Since multi-engine aircraft offer propulsion unit redundancy, the previously cleaned DataFrame (`df_clean`) is sliced to remove all entries for single-engine aircraft. The analytics and visualization operations are performed on the modified DataFrame (`df_modified`) to yield insights on the least safe multi-engine aircraft models.

## Objective 2
### Most Safe Aircraft Models
* The aggregate sum of survivors `Total.Uninjured` for each `Make` and `Model` is sorted in descending order (ascending = False) and filtered (head = 10) to select the top-10 safest aircraft in terms of cumulative survivors from aircraft accidents and incidents.
* Using Seaborn, a horizontal barplot visualizes the top 10 safest aircraft the company can consider procuring.

Since multi-engine aircraft avail propulsion unit redundancy, the previously cleaned DataFrame (`df_clean`) is sliced to drop all entries for single-engine aircraft. The analytics and visualization operations are performed on the modified DataFrame (`df_modified`) to yield insights on the safest multi-engine aircraft models.


## Objective 3
### Recommended Aircraft Model to Purchase 
* The company’s portfolio diversification strategy involves purchasing and operating an airplane fleet for commercial and private enterprises.
* Per the company’s target market, its new aviation division will majorly offer services spanning Executive/corporate flights, Business flights, and Aerial applications.
* Owing to unique operational complexities and logistical considerations, the safest aircraft models are not universally applicable.
* Thus, the dataset is filtered for the three relevant `Purpose.of.flight` aviation services the company will typically offer its clients.
* The `.groupby ()` method is leveraged to group each of the filtered `Purpose.of.flight` aviation service, `Make`, and `Model` to determine the safest aircraft model for each application.
* The aggregate sum of survivors `Total.Uninjured` for each `Make` and `Model` are sorted in descending order (ascending = False) and filtered (head = 10) to select the top-10 safest aircraft in terms of cumulative survivors.
* The safest aircraft for each `Purpose.of.flight` is visualized using the Seaborn library.


Since multi-engine aircraft avail propulsion unit redundancy, the previously cleaned DataFrame (`df_clean`) is sliced to drop all entries for single-engine aircraft. The analytics and visualization operations are performed on the modified DataFrame (`df_modified`) to yield insights on the safest multi-engine aircraft models concerning particular applications.




## Interpretation 
The analysis yields three recommendations on the aircraft models the company should procure and operate after entering the commercial aviation industry.
<strong> The CESSNA-560XL aircraft is recommended for Executive/ Corporate flights: </strong> The baseline and modified model confirm the aircraft is safest for executive and corporate flights.
<strong> The DEHAVILLAND DHC-8-311 aircraft is recommended for Business Flights: </strong> The baseline and modified model conform the aircraft is safest for business flights.
<strong> The CESSNA-A188B aircraft is recommended for Aerial Applications: </strong> The modified model proposes the MCDONNELL DOUGLAS-DC 10-10 (a three-engine, 250-seater) aircraft for aerial applications. The proposed alternative by the modified model is rejected because aerial applications typically include agricultural activities such as spraying crop fields. Hence, the single-egine CESSNA-A188B is recommended for aerial applications.


## Next Steps
* Consult key stakeholders in the aircraft manufacturing sector on the safest engine types per current engineering standards and inquire whether they can be fitted to the proposed airplane models.
* Performing market research to determine the number of units to purchase for each proposed aircraft.
* Collaboration with stakeholders in the commercial aviation sector, the company’s shareholders to source capital for facilitating diversification strategy, and the human resource department to recruit adequately skilled personnel to operate the proposed aircraft models.
