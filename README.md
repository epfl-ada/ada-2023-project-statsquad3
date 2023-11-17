# ADA 2023 Project — Team statsquad3

## Abstract:

Our research project focuses on Wikispeedia, a game that reflects our contemporary patterns of consuming digital content. In the fast-paced information era, we often find ourselves bombarded with news, social media updates, and a seemingly endless stream of digital content. It's commonly observed that the information that leaves a lasting impact on us is that which evokes strong emotions. Our hypothesis is rooted in this observation, suggesting that Wikispeedia players might be influenced by the emotional tone of Wikipedia articles, choosing paths in the game that are not only relevant in terms of content but also emotionally engaging.

The first step in our study is to evaluate the emotional tone of Wikipedia pages. While Wikipedia aims for neutrality, the human element in writing these articles can inadvertently introduce positive or negative biases. We plan to use the ######InsertDataset###### tool to assign a positivity score to each Wikipedia page in our dataset. This will help us determine the overall sentiment of the pages.

After establishing these positivity scores, our next goal is to investigate whether these sentiments subtly influence how players navigate through Wikispeedia. Previous research, as mentioned in ######Insert article name######, indicates that players tend to create paths that are semantically coherent. Our study aims to expand on this by exploring the possibility that the emotional tone of the articles also plays a role in shaping these paths.

This research could provide new insights into the impact of emotional content on user interaction and decision-making in digital environments. Understanding how sentiments embedded in digital content affect user choices could be pivotal in comprehending our broader engagement with the internet and digital platforms. It could reveal underlying patterns in how we process and respond to digital information, particularly in games and informational websites like Wikispeedia.

___

## Questions to answer:
"Is a Wikispeedia game path correlated to the positivity/negativity of the target topic?"
- Does the sentiment of the starting article influence the trajectory of the game path? For instance, if a player begins with an article with a negative tone, are they more likely to navigate through similarly toned articles?
- How do neutral-toned articles fit into the path structure? Are they more likely to be used as transitional nodes between positive and negative articles?
- Can we observe any consistent emotional arcs in the paths (e.g., starting positive, dipping into negative, and then ending positively)?
- Are there noticeable patterns of sentiment oscillation in the paths chosen by players? For instance, do players often navigate through contrasting sentiments to reach their target, such as starting from an article with a negative tone like “Hell” to reach a positive one like “Paradise”?
- How does the sentiment score of a target topic affect the structure and nature of the path chosen by players? Is there a relationship between the extremity of a target article's sentiment (highly positive/negative) and the length of the path taken to reach it? When players choose shorter paths, are these paths characterized by articles with, for example, more extreme sentiment scores?
- Are certain categories or themes within Wikipedia consistently associated with similar sentiment scores? For example, do topics like fruits generally have a positive tone, while others might trend towards neutrality or negativity? 

## Methods:
### 1st step: Sentiment Analysis
The first step of our analysis is to find a reliable method to perform sentiment analysis of the given Wikispeedia articles. Each member of our group chose a different method for sentiment analysis, and we tested these methods over a sample of articles that we labeled. Here's a brief overview of each method:

- Word Lexicon Method: This technique involves using a lexicon, a collection of words that have been tagged with scores to reflect their sentiment polarity. Words or phrases in a text are labeled as positive, negative, or sometimes neutral based on a valence dictionary. This approach is straightforward and rule-based, where the overall sentiment is calculated based on the polarity scores of the words in the document​​​​​​.

- Pattern Method: Pattern is a multipurpose library for natural language processing that includes sentiment analysis. Its sentiment function assesses text sentiment by tokenizing the text, normalizing for case, and consulting a sentiment dictionary to score each word on polarity and subjectivity. The average of these scores reflects the overall sentiment of the text, with polarity indicating the emotional direction (positive or negative) and subjectivity the strength of emotion. Pattern is known for its robustness and has been widely used for over a decade.

- VADER (Valence Aware Dictionary and sEntiment Reasoner): VADER is a lexicon and rule-based sentiment analysis tool specifically designed for social media content. It is sensitive to both the polarity (positive/negative) and intensity (strength) of emotions. This method uses a sentiment lexicon which is a list of lexical features, like words, that are generally labeled with their sentiment intensity. It is known for its effectiveness in handling social media texts and other domains where expressions are less formal and more emotionally varied​​​​​​.

- RoBERTa (A Robustly Optimized BERT Pretraining Approach): RoBERTa is an advanced AI model developed by the Meta Research team, which is trained on a vast corpus of data for self-supervised natural language processing. It performs binary sentiment analysis, categorizing text as either positive or negative. RoBERTa has been fine-tuned on millions of tweets and is particularly suitable for analyzing English-language texts from various sources, including social media​​​​​​.

- LIWC (Linguistic Inquiry and Word Count): LIWC is a transparent text analysis program that counts words in psychologically meaningful categories. It's considered a gold standard in software for analyzing word use, able to detect meaning in various experimental settings. This method is particularly adept at showing attentional focus, emotionality, social relationships, thinking styles, and individual differences in texts​​​​​​.

### 2nd step: Sentiment Scoring and Data Compilation
The foundation of our analysis is the sentiment scoring of individual Wikipedia articles within the Wikispeedia dataset. Utilizing sentiment analysis tools, we have to score each article for polarity and subjectivity. Concurrently, we will collect extensive game path data, noting the sequence of articles, the starting and ending points, and path lengths. This dual approach of sentiment scoring and game path data collection allows us to establish a comprehensive dataset where each article's sentiment is mapped to its occurrence within game paths. This meticulous mapping is critical as it sets the stage for our subsequent analysis and ensures we have a robust dataset from which to draw our conclusions.

### 3rd step: Sentiment Trajectory and Pattern Analysis
With our dataset in hand, we delve into the core of our investigation: the sentiment trajectory and pattern analysis. This phase involves a detailed examination of how the sentiment of starting articles influences the trajectory of the game path. We'll analyze if players show a preference for maintaining a consistent emotional tone throughout their navigation. The role of neutral articles as potential transitional nodes between emotionally charged articles will also be assessed. We will look for oscillating patterns where paths may swing between positive and negative sentiments and correlate the extremity of article sentiments with the characteristics of the paths, such as their length. This phase is analytical and exploratory, relying on both quantitative methods like statistical modeling to assess the significance of patterns and qualitative insights from player behavior studies.

### 4th step: Thematic Analysis and Predictive Modeling
The final phase moves beyond individual paths to look at broader trends and predictions. We will group articles by categories or themes, analyzing whether certain topics are consistently associated with particular sentiment scores. Machine learning classification techniques will be utilized to classify game paths based on sentiment and potentially predict future path choices based on the sentiment of starting articles. We will also establish sentiment score thresholds that have a significant impact on path selection. This phase is aimed at synthesizing our findings into a cohesive understanding of the sentiment's influence on navigational behavior in Wikispeedia. Through this, we aim to offer a nuanced view of how sentiment can steer user engagement in interactive platforms, providing insights that could have implications for content creation and game design.



## Additional dataset:

For our sentiment analysis project within the Wikispeedia framework, we will be primarily utilizing two key datasets. The first essential dataset is a sentiment dictionary, which will serve as the foundation for our analysis tools. This lexicon will consist of a comprehensive list of words, each tagged with a sentiment score that denotes its associated emotional weight. The dataset will integrate existing sentiment lexicons and may also include new entries tailored to the context of our project, ensuring that our sentiment analysis is both robust and nuanced. The second is a sentiment score dataset for each Wikipedia article in the Wikispeedia database. This dataset will be meticulously compiled using a variety of sentiment analysis tools such as Pattern, VADER, LIWC, and RoBERTa. Each article will be evaluated to ascertain its polarity, indicating the positivity or negativity of the content, and its subjectivity, reflecting the intensity of emotion conveyed. Together, these datasets will allow us to paint a detailed picture of the emotional landscape across the Wikispeedia articles and understand how it influences user navigation and engagement.

## Timeline and organisation:

Below we present an outlined timeline for the forthcoming weeks, detailing the distribution of tasks and how we intend to allocate responsibilities.

Week 1: Initiation of sentiment scoring and data compilation (Step 2)
The first week will be dedicated to setting up our analysis infrastructure. We'll begin by sentiment scoring the Wikipedia articles using our selected tools. Each team member will be responsible for a portion of the dataset to ensure parallel processing and efficiency. Concurrently, we will start gathering game path data from the Wikispeedia database.

Week 2: Completion of data compilation and preliminary aAnalysis (Step 2)
In our second week, we will wrap up any remaining sentiment scoring and finalize the game path data compilation. With the completed dataset, we'll conduct a preliminary analysis to identify any immediate patterns that can inform our more detailed investigation in the following week.

Week 3: Detailed sentiment trajectory and pattern analysis (Step 3)
Our third week will focus on the heart of our research—sentiment trajectory and pattern analysis. We'll delve into the sentiment data aligned with game paths, examining the influence of starting article sentiment and the role of neutral articles. The week will culminate in the application of statistical models to determine the significance of our findings.

Week 4: Thematic analysis, predictive modeling, and report drafting (Step 4)
In our final week, we will extend our analysis to include thematic categorization and initiate predictive modeling using machine learning techniques. Additionally, we will begin drafting our comprehensive report, with each team member contributing insights from their work. By the end of this week, we aim to have a finalized draft ready for review and submission.

Regular team meetings will be held each week to ensure alignment, with task distribution based on individual strengths and areas of expertise to maintain balanced workloads and optimal collaboration.





