The main notebook is ```main.ipynb```.<br>
Data story link: https://yrymax.github.io/ada-project-statsquad3/.

# ADA 2023 Project — Team statsquad3 — "Objectivity through the emotional lens: How does the sentiment of Wikispeedia articles affect player game paths?"

## Abstract:

We believe Wikispeedia mirrors the way we consume content in 2023. Today, information comes to us continuously through mass notifications, endless scrolling, and mindless digital consumption. Therefore, information that sticks is information that shocks. We think Wikispeedia hides this same idea, but transposed and expressed through the game paths. We hypothesise that players use paths not only semantically meaningful, but also sentimentally powerful.

Our project consists of analysing game paths through the lens of sentiment analysis scores of wikipedia page contents. In a first part, we presented various methods for assigning a sentiment scores to each Wikispeedia article (milestone P2). In a second part, we explore and analyse how and if this sentiment (whether it is there intentionally or not) influences how people play the game (this milestone).

This could provide new insights into decision-making in textual environments. Understanding how sentiments embedded in digital content affect user choices could be pivotal in comprehending our broader engagement with the internet and digital platforms.

___

#### Some subquestions we aim to answer:
1. Does the sentiment of the starting article influence the trajectory of the game path? For instance, if a player begins with an article with a negative tone, are they more likely to navigate through similarly toned articles?
2. Can we observe any consistent emotional arcs in the paths (e.g., starting positive, dipping into negative, and then ending positively)?
3. Are there noticeable patterns of sentiment oscillation in the paths chosen by players? For instance, do players often navigate through contrasting sentiments to reach their target, such as starting from an article with a negative tone like “Hell” to reach a positive one like “Paradise”?
4. How does the sentiment score of a target topic affect the structure of the path chosen by players? Is there a relationship between the extremity of a target article's sentiment (highly positive/negative) and the length of the path taken to reach it? When players choose shorter paths, are these paths characterized by articles with, for example, more extreme sentiment scores?
5. Are certain categories or themes within Wikipedia consistently associated with similar sentiment scores? For example, do topics like fruits generally have a positive tone, while others might trend towards neutrality or negativity? 

## Methods:
### Sentiment Analysis
In the first step of our analysis, we explored various methods to perform sentiment analysis of the given Wikispeedia articles. This step was crucial for obtaining interpretable and reliable results in the next part. Each member of our group tackled a different method for sentiment analysis, and we tested these methods over a sample of articles that we labeled. Here are the different methods (details are provided in the notebook ```main_milestone_2.ipynb```):

- Word Lexicon
- Pattern
- VADER
- LIWC
- RoBERTa

After this stage, we decided to select the RoBERTa method for inferring the articles' sentiment scores. It gave the best results on our small, manually labelled test set, and had the benefit of giving an interesting, "separable" distribution of the scores among articles (see notebooks).

### Sentiment Trajectory and Pattern Analysis for each subquestion: (each number corresponds to the subquestion above)
1. To determine the possible effect of the starting article on the paths score, both the positivity and the negativity of the paths are analysed. For this, the distributions of the positive/negative percentage of the paths are compared with man-whithney tests to deduct their independance (or not).
2. To investigate common emotional paths in Wikispeedia patterns, we initially conducted a basic analysis focusing on the average sentiment values across all paths. However, seeking more meaningful insights, we shifted to clustering the data, which allowed us to uncover and analyze more significant and nuanced emotional trends.
3. To determine whether users' paths exhibit noticable oscillation, we performed a significance test on the distribution of user-selected links versus the original network links. Additionally, we conducted regression analyses on various models to identify factors that influence path oscillation.
4. To analyse the effect of the target article's sentiment on the game structure, we perform a causal analysis by making a tool for viewing paths, and performing regression analysis to determine the significance of our observations.
5. It is known that Wikipedia articles cover a wide range of topics, and sentiment within these articles of the same topic can be consistent with the subject matter. To investigate how sentiment is prominent within a topic, we utilised the topic data from categories.tsv dataset and studied the sentiment score of these extracted topics at different level of generality.

## Additional dataset:

There are no direct additional datasets. The only external datasets we use are the lexicons used by some of the sentiment analysis tools. 

## Organisation and contribution of each member:

In general, we split the tasks among the different research subquestions and sentiment analysis methods. Everyone contributed to the visualizations and descriptions of their own sections in the data story website, and overall everyone contributed to delineating a story out of our individual findings to make it a smooth story.

- Minh: sentiment analysis method 3 (VADER), research subquestion 5

- Arnaud: sentiment analysis method 4 (LIWC), research subquestion 1

- Renyi: sentiment analysis method 2 (pattern), research subquestion 3

- Alexandre: sentiment analysis method 1 (word lexicon), research subquestion 4

- Brando: sentiment analysis method 5 (RoBERTa), research subquestion 2

