# ADA 2023 Project — Team statsquad3

## Abstract:

We believe Wikispeedia mirrors the way we consume content in 2023. Today, information comes to us continuously through mass notifications, endless scrolling, and mindless digital consumption. Therefore, information that sticks is information that shocks. We think Wikispeedia hides this same idea, but transposed and expressed through the game paths. We hypothesise that players use paths not only semantically meaningful, but also sentimentally powerful.

Our project consists of analysing game paths through the lens of sentiment analysis scores of wikipedia page contents. First, we present various methods for assigning a sentiment scores to each Wikispeedia article (this milestone). Second, we aim to determine if this sentiment (whether it is there intentionally or not) influences how people play the game. In order to do this, we aim to leverage the research in [1], which presents a method for obtaining semantic similarities between articles, allowing us to characterise a game path.

This could provide new insights into decision-making in textual environments. Understanding how sentiments embedded in digital content affect user choices could be pivotal in comprehending our broader engagement with the internet and digital platforms.

___

## Main research question

"How does the sentiment of Wikispeedia articles affect player game paths?"

#### Some subquestions we aim to answer:
1. Does the sentiment of the starting article influence the trajectory of the game path? For instance, if a player begins with an article with a negative tone, are they more likely to navigate through similarly toned articles?
2. How do neutral-toned articles fit into the path structure? Are they more likely to be used as transitional nodes between positive and negative articles?
3. Can we observe any consistent emotional arcs in the paths (e.g., starting positive, dipping into negative, and then ending positively)?
4. Are there noticeable patterns of sentiment oscillation in the paths chosen by players? For instance, do players often navigate through contrasting sentiments to reach their target, such as starting from an article with a negative tone like “Hell” to reach a positive one like “Paradise”?
5. How does the sentiment score of a target topic affect the structure and nature of the path chosen by players? Is there a relationship between the extremity of a target article's sentiment (highly positive/negative) and the length of the path taken to reach it? When players choose shorter paths, are these paths characterized by articles with, for example, more extreme sentiment scores?
6. Are certain categories or themes within Wikipedia consistently associated with similar sentiment scores? For example, do topics like fruits generally have a positive tone, while others might trend towards neutrality or negativity? 

## Methods:
### Sentiment Analysis
The first step of our analysis is to find a reliable method to perform sentiment analysis of the given Wikispeedia articles. This step is crucial for obtaining interpretable results in the next parts. Each member of our group tackled a different method for sentiment analysis, and we tested these methods over a sample of articles that we labeled. Here's a brief overview of each method:

- Word Lexicon Method: using a positive and negative score for each word in a lexicon, the individual token scores are summed for each article.

- Pattern Method: Pattern is a python package that leverages a sentiment dictionary to score each word on polarity and subjectivity. Polarity (emotional direction (positive or negative)) and subjectivity (strength of emotion) are particularly interesting in the case of wikipedia.

- VADER (Valence Aware Dictionary and sEntiment Reasoner): VADER is a lexicon and rule-based sentiment analysis tool specifically designed for social media content. It is sensitive to both the polarity (positive/negative) and intensity (strength) of emotions. This method uses a sentiment lexicon which is a list of lexical features, like words, that are generally labeled with their sentiment intensity. It is known for its effectiveness in handling social media texts and other domains where expressions are less formal and more emotionally varied​​​​​​.

- RoBERTa (A Robustly Optimised BERT Pre-training Approach): RoBERTa is a large language model (Meta Research), which is trained on a vast corpus of data for self-supervised natural language processing. It performs binary sentiment analysis, categorising text as either positive or negative. RoBERTa has been fine-tuned on millions of tweets, making it suitable to detect sentiment.

- LIWC (Linguistic Inquiry and Word Count): LIWC counts words in psychologically meaningful categories. This method is particularly adept at showing attentional focus, emotionality, social relationships, thinking styles, and individual differences in texts​​​​​​.

### Sentiment Scoring on whole data
Inferring the sentiment on the whole data can help us visualise better these scores and refine the answers to our research questions. At this stage we aim to select one scoring method and use it for the remainder of the project. (see questions below)

### Sentiment Trajectory and Pattern Analysis for each subquestion: (each number corresponds to the subquestion above)
1. 
2.
3.
4.
5.
6.

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

