# Screen Tastes: The User-Critic Divide in Cinema
[![Github Pages](https://github.com/epfl-ada/ada-2023-project-radatouille/actions/workflows/deploy.yml/badge.svg)](https://github.com/epfl-ada/ada-2023-project-radatouille/actions/workflows/deploy.yml)


by the *Radatouille* team

## Abstract

In the age of abundant cinematic content, distinguishing exceptional movies becomes a complex task. This project aims to demystify the intricate metrics used to assess movie quality. Our motivation stems from the challenge faced by viewers in selecting films that align with their preferences, given the varying opinions of critics, audiences, and commercial success. We intend to weave a narrative exploring how different quality metrics, such as box office performance, audience ratings, and critical reviews, interplay and influence movie perception. Another metric can be the awards and nominations from different known film awards. By analyzing these diverse indicators, our goal is to uncover patterns and anomalies that dictate a movie's success and recognition, thus offering a comprehensive view of what constitutes a 'good' movie in different spheres (cinephiles, experts, critics).

Certainly, I'll add descriptive text to the tree structure to align it with your template format:

## Repository Structure

- `README.md`: Main documentation file of the repository, providing an overview and general instructions.
- `milestone_2.ipynb`: Main notebook for Milestone 2.
- `scrap.ipynb`: Notebook for scraping scripts.
- :file_folder: `data`:
  - :file_folder: `external`: external data sources
    - `metacritic_reviews.csv`: Review data scraped from Metacritic.
    - `title.ratings.tsv`: Title ratings information from IMDb.
    - `wikidata_awards.csv`: Award-related data scraped from Wikidata.
    - `imdb_awards.csv`: Award-related data scraped from IMDb.
  - :file_folder: `preprocessed`: preprocessed data
    - `character.metadata.preprocessed.tsv`: Character metadata in a preprocessed format.
    - `movie.metadata.preprocessed.tsv`: Movie metadata, structured and cleaned.
    - `plot_summaries.preprocessed.txt`: Text summaries of plots, formatted for analysis.
  - :file_folder: `processed`: processed data
    - `cmu_movies.csv`: Comprehensive dataset of movies.
    - `cmu_movies_augmented.csv`: Augmented movie dataset with additional metadata.
  - :file_folder: `raw`: raw data files, unprocessed and in original form.
    - `character.metadata.tsv`: Original character metadata.
    - `movie.metadata.tsv`: Initial movie metadata file.
    - `name.clusters.txt`: Text file containing name clusters.
    - `plot_summaries.txt`: Raw text files of movie plot summaries.
    - `README.txt`: Descriptive file providing details about the CMU Dataset.
    - `tvtropes.clusters.txt`: Cluster data related to TV tropes.


## Research Questions
- What kind of movies do users like?
- What kind of movies do critics like?
- Do the different critics have the same tastes?
- Which films are most likely to win awards?
- Do users and awards agree?
- Do critics and awards agree?

## Proposed additional datasets (if any):
As our project's goal is to compare different metrics that we don't originally have, we will need to get data from different sources. We will use the following datasets:
- Average user's score:
    - Scrapped from [IMDb](https://www.imdb.com/)
- Average critics's score:
    - Scrapped from [IMDb](https://www.imdb.com/)
    - IMDb get this score from the website [metacritic](https://www.metacritic.com/)
- Total number of nominations and awards:
    - Scrapped from [IMDb](https://www.imdb.com/)
- Number of nomination and awards for some specific awards (Oscar, Cesar, ...):
    - Scrapped from wikidata's API

We decided to work only with movies with exploitable data, i.e. data that has a freebase id, an imdb id and a metacritic id. We end up with around 8'000 movies.

## Methods
We will subdivise our project in different steps in order to answer the question. The numbered notation will be used to refer to the different steps in the rest of the document.
1. **Getting familiar with the data and exploring external datasets possibilities**: We will explore the data we have and see what we can do with it, what we cannot, and start to clean the dataset. We will also explore the different external datasets we can use.
2. **Data scrapping and pre-processing**: We will scrap the data from IMDb and metacritic and merge it with our data.
Additionnaly we pre-process the data in order to have an exploitable dataset, and avoid having outliers. 
3. **Comparing different metrics and metadata**: 
The different metrics we will compare are:
    - A: User's score
    - B: Critics's score
    - C: Awards's score: we will consider the number of winning and nomination for some famous awards (Oscar, Cesar, ...).
    
    We will try to see for each metric if there is a correlation between the different metadata and the metric. We will also try to discern some eventual biases in the different metrics.

    The number of awards and of nominations is considered as a metric. It is a good indicator of the quality of a movie, as the box office revenue is a good indicator of the success of a movie.

4. **Comparing different metrics between them**: We will try to see if there is a correlation between the different metrics.
    - A: Awards and user's average rating
    - B: Awards and critics's average rating
    - C: User's average rating and critics's average rating
    - D: Different type of awards between themself (Oscar, Cesar, ...)
5. **Datastory**: Creating a datastory
6. **Website**: Creating a website
7. **Project logistics**: Aggregating each step in a notebook

## Proposed timeline

The deadline is **December 22nd.**


| Deadline                 | Description               |
| ---------------------- | ------------------------- | 
| Nov. 12th |  Step 1. |
| Nov. 17th | Step 2. + Milestone 2 |
| Nov. 26th | Step 3. |
| Dec. 01st | Homework 2. |
| Dec. 10th   | Step 4. |
| Dec. 17th   | Step 5. |
| Dec. 22nd   |   Step 6. + Step 7|


## Organization within the team
We use the steps described above to divide the work between us.
We will work together on the datastory and the website.

We use the following acronyms for first names to make them easier to read:
- Antonin: A
- Baptiste: B
- Enzo: E
- Jamil: J
- Mariella: M

| What?                 | Who?               |Statuts |
| --------------------- | ------------------ |--------|
| Step 1. | Everyone | **Done** |
| Step 2. | A + B| **Done** |
| Step 3. A| A + J | *Ongoing* | 
| Step 3. B| E + J | *Ongoing* |
| Step 3. C | E + M + B | *Ongoing* |
| Step 4. A | A + E | To do |
| Step 4. B | M + E | To do |
| Step 4. C | B + J | To do |
| Step 4. D | B + M | To do |
| Step 5. | J + M | To do |
| Step 6. | A + B + E | To do |
| Step 7. | Everyone | To do |

## Questions for TAs (optional): 
- We thought of additionnal stuff we could do, like scrapping text reviews and doing some NLP on them, but at this moment it's a bit hard to estimate if that's realistic feasible in term of time. Can we do some additionnal stuff if we have time, or should we focus on the main steps that we announced here? 
