# Screen Tastes: The User-Critic Divide in Cinema

by the *rADAtouille* team

[![Github Pages](https://github.com/epfl-ada/ada-2023-project-radatouille/actions/workflows/deploy.yml/badge.svg)](https://github.com/epfl-ada/ada-2023-project-radatouille/actions/workflows/deploy.yml)

## Abstract

In the age of abundant cinematic content, distinguishing exceptional movies becomes a complex mission, and most of the time critics and average users don’t agree on the quality of a movie. This project aims to demystify this difference and try to understand which parameter influences this difference. We will study the effect of different features such as the movie genre, awards, country, tropes (element of a story), release year, actor, languages, etc… on this difference. By analyzing these diverse features, our purpose is to uncover patterns and anomalies that dictate a movie's success and recognition, thus offering a comprehensive view of what constitutes a 'good' movie in different spheres (cinephiles, experts, critics).


## Repository Structure

<insérer le truc de chat GPT>


## Research Questions



* Do users and critics have different tastes?
* If yes, how does each of these features impact the difference independently?
* Finally, can we find global features explaining that discrepancy and how well?


## Proposed additional datasets:

As our project's goal is to compare different metrics that we don't originally have, we will need to get data from different sources. We will use the following datasets:



* Average user's score:
    * Scrapped from IMDb
* Average critics's score:
    * Scrapped from IMDb
    * IMDb got this score from the website Metacritic
* Total number of nominations and awards:
    * Scrapped from IMDb
* Number of nominations and awards for some specific awards (Oscar, Cesar, ...):
    * Scrapped from Wikidata's API
* Tropes:
    * Found on [Github](https://github.com/dhruvilgala/tvtropes), annotated by hand from a paper:
        * Gala, D., Khursheed, M. O., Lerner, H., O'Connor, B., & Iyyer, M. (2020). Analyzing Gender Bias within Narrative Tropes. Association for Computational Linguistics. You can find more information about the paper [here](https://www.aclweb.org/anthology/2020.nlpcss-1.23).
* We decided to work only with movies with exploitable data, i.e. data that has a freebase ID, an IMDb ID, and a Metacritic ID. We ended up with around 8'000 movies.


## Structure

We subdivide our project into different steps to answer the question. The numbered notation will be used to refer to the different steps in the rest of the document.



1. **Getting familiar with the data and exploring external dataset possibilities**: We explore the data we have and see what we can do with it, and what we cannot, and start to clean the dataset. We also explore the different external datasets we can use.
2. **Data scrapping and pre-processing:** We scrap the data from IMDb,  Wikidata, and get the additional dataset from Github, and merge it with our data. Additionally, we pre-process the data to have an exploitable dataset and avoid having outliers.
3. **Comparing different metrics and metadata:** After an initial analysis of the used metrics (User’s and critics’s score), we will create a new metric that reflects the difference between both metrics. 

    We try to see if for the created metric there is a correlation between the different metadata and the metric. We will also try to discern some eventual biases in the different metrics.


    The number of awards and nominations is considered as an additional metadata. It is a good indicator of the quality of a movie.

4. Comparing different metrics between them: we try to see which features have the biggest effect on the rating difference.
5. Datastory: Creating a data story
6. Website: Creating a website
7. Project logistics: Aggregate each step in a notebook, comment on the code, and adapt this README!


## Methods


### T-Test

Test to verify if the mean of 2 groups is significantly the same or not.


### Pearson Correlation

Measurement of the linear correlation between 2 groups. Has been used especially to select the most interesting features.


### Ordinary Least Squares (OLS) regression

Extract the relative impact of each feature on a variable of interest. It is important to keep in mind that the OLS regression is super sensitive to outliers and multicollinearity. Such problems can be addressed using regularization (Lasso or Ridge).


### Variance Inflation Factor (VIF)

Measurement of the multicollinearity of a feature. Has been used to get rid of the multicollinear features that are threatening the OLS regression.


## Contribution

|Teammate | Contribution |
|--------|--------------|
|Antonin | <ol><li>External dataset scrapping</li><li>External dataset research</li><li>Data exploration</li><li>Statistical interpretation for OLS & Pearson</li><li>Website</li></ol>|
|Baptiste | <ol><li>External dataset scrapping</li><li>Basic data exploration</li><li>Specific feature analysis</li></ol>|
|Enzo     | <ol><li>Data exploration</li><li></li><li>TODO</li><ol>|
|Jamil     | <ol><li>TODO</li><li>TODO</li><li>TODO</li></ol>|
|Mariella | <ol><li>TODO</li><li>TODO</li><li>TODO</li></ol>|
