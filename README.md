# ADA 2023 Project — Team statsquad3

## Abstract:
Our project consists of analysis based on the positivity score of wikipedia pages. Indeed, wikipedia pages are supposed to be neutral, however they are still written by human, who will sometimes unintentionally create a positive or negative bias. The first step is therefore to assign a positivity score to each of the wikipedia page in the dataset. This is done with the use of ?InsertDataset?.
The goal is then to see if this positivity (conciously or unconciously) influences how people play the game. From the article ?Insert article name?, we know that most of the path created by plays are sementically related.

Questions to answer: "Is a Wikispeedia game path correlated to the positivity/negativity of the target topic?"
- Are related topics associated with a similar positivity score? (e.g. fruits are positive?)
- How does target-topic-positivity influence the game path?
- Are highly positive/negative targets associated with shorter paths?
- Do shorter paths take more extremely positive words?
- Are there “oscillating” paths? (e.g. to find “Paradise” you can first look for “Hell”)

Methods:
### 1st step
Associate a positiveness/negativeness score for each wikipedia page using its textual content

Additional dataset:
⇒ Use an external dataset for first step: some form of sentiment analysis dataset 
list of positive words, list of negative words (ex: Opinion Lexicon)
pre-existing model for inferring positiveness/negativeness of text (ex: ChatGPT plug-in)

Timeline and organisation:


Our story:
We believe Wikispeedia mirrors the way we consume content in 2023. Today, information comes to us continuously through mass notifications, endless scrolling, and mindless digital consumption. Therefore, information that sticks is information that shocks. We think Wikispeedia hides this same idea, but transposed and expressed through the game paths. We hypothesize that players use paths not only semantically meaningful, but also sentimentally powerful. 
