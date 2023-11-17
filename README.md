Note: the main notebook is ```main.ipynb```.

# ADA 2023 Project — Team statsquad3 — "Objectivity through the emotional lens: How does the sentiment of Wikispeedia articles affect player game paths?"

## Abstract:

We believe Wikispeedia mirrors the way we consume content in 2023. Today, information comes to us continuously through mass notifications, endless scrolling, and mindless digital consumption. Therefore, information that sticks is information that shocks. We think Wikispeedia hides this same idea, but transposed and expressed through the game paths. We hypothesise that players use paths not only semantically meaningful, but also sentimentally powerful.

Our project consists of analysing game paths through the lens of sentiment analysis scores of wikipedia page contents. First, we present various methods for assigning a sentiment scores to each Wikispeedia article (this milestone). Second, we aim to determine if this sentiment (whether it is there intentionally or not) influences how people play the game.

This could provide new insights into decision-making in textual environments. Understanding how sentiments embedded in digital content affect user choices could be pivotal in comprehending our broader engagement with the internet and digital platforms.

___

#### Some subquestions we aim to answer:
1. Does the sentiment of the starting article influence the trajectory of the game path? For instance, if a player begins with an article with a negative tone, are they more likely to navigate through similarly toned articles?
2. How do neutral-toned articles fit into the path structure? Are they more likely to be used as transitional nodes between positive and negative articles?
3. Can we observe any consistent emotional arcs in the paths (e.g., starting positive, dipping into negative, and then ending positively)?
4. Are there noticeable patterns of sentiment oscillation in the paths chosen by players? For instance, do players often navigate through contrasting sentiments to reach their target, such as starting from an article with a negative tone like “Hell” to reach a positive one like “Paradise”?
5. How does the sentiment score of a target topic affect the structure and nature of the path chosen by players? Is there a relationship between the extremity of a target article's sentiment (highly positive/negative) and the length of the path taken to reach it? When players choose shorter paths, are these paths characterized by articles with, for example, more extreme sentiment scores?
6. Are certain categories or themes within Wikipedia consistently associated with similar sentiment scores? For example, do topics like fruits generally have a positive tone, while others might trend towards neutrality or negativity? 

## Methods:
### Sentiment Analysis
The first step of our analysis is to find a reliable method to perform sentiment analysis of the given Wikispeedia articles. This step is crucial for obtaining interpretable results in the next parts. Each member of our group tackled a different method for sentiment analysis, and we tested these methods over a sample of articles that we labeled. Here are the different methods (details are provided in the main notebook):

- Word Lexicon
- Pattern
- VADER
- LIWC
- RoBERTa

### Sentiment Scoring on whole data
Inferring the sentiment on the whole data can help us visualise better these scores and refine the answers to our research questions. At this stage we aim to select one scoring method and use it for the remainder of the project. (see questions below)

### Sentiment Trajectory and Pattern Analysis for each subquestion: (each number corresponds to the subquestion above)
1. For each path, the score of the starting article is compared to the other articles scores. Check if most articles are in the same range of the starting article (for example with root article with sentiment 0.74, then are most following articles in [0.64,0.84]?)
2. This question is perhaps the one that will require the most creativity in visualisation, or path representation. We could use a dense embedding of the paths to derive some results for this question.
3. Several logic patterns could be manually created (for instance: starting positive then consistently going to negative) and compared to the real paths. A possible framework is: given a pattern, normalise by the size, compute the MSE over the path, if the error is below a certain threshold, then the path fits the pattern.
4. In all paths, check the extremes (|s|>0.8 for instance), look at the following and previous article scores, then we can say it is oscillating if previous or subsequent article is also extreme. The percentage of extreme articles followed/preceded by extreme articles could answer the question.
5. Derive a sentiment extremeness score ($|s|$ for instance) and the rest is similar as above.
6. We perform some clustering on the articles by their content (perhaps using another language model). Then it suffices to describe and analyse the distribution of the scores in each cluster, perhaps perform some hypothesis testing.

## Additional dataset:

There are no direct additional datasets. The only external datasets we use are the lexicons used by some of the sentiment analysis tools. 

## Timeline and organisation:

Week 1: sentiment scoring of the whole dataset with different methods, visualisations will help us determine what method to keep.

Week 2: split tasks across research sub-questions (see above), make visualisations to see which questions are the most interesting, give
a strong causal conclusion to each research question.

Week 3: Detailed sentiment trajectory and pattern analysis for the interesting sub questions. We'll delve into the sentiment data aligned with game paths, examining the influence of sentiments. We will try to make statistical models to answer specific questions.
Predictive models can be made to help generating the user path for a random pair of articles.

Week 4: Devise a data story from the analyses such that it is aligned with our statistical findings. Begin the webpage.

Week 5: Cleaning the repository and wrapping up the data story webpage, host cohesive and interactive visualisations to display our outcome.

## Questions for TA
Should we select one sentiment scoring method or consistently compare the methods through all the analyses?

