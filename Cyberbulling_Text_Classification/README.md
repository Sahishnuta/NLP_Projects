## Problem Statement

**Cyberbullying Text Classification**

The project aims to develop a machine learning system that can automatically detect and classify cyberbullying content in social media text. The system analyzes textual data to identify whether a given piece of text contains cyberbullying content, and if so, categorizes it into specific types of cyberbullying.

### Key Objectives:

1. **Binary Classification**: Detect whether text contains cyberbullying or not
2. **Multi-class Classification**: Categorize cyberbullying into specific types including:
   - Age-based bullying
   - Ethnicity-based bullying  
   - Gender-based bullying
   - Religion-based bullying
   - Other types of bullying
   - Not cyberbullying

### Technical Approach:

The project implements a comprehensive NLP pipeline with multiple approaches:

1. **Traditional ML Models**: 
   - Logistic Regression
   - Random Forest
   - Support Vector Machines (SVM)
   - Naive Bayes

2. **Deep Learning Models**:
   - LSTM (Long Short-Term Memory) networks
   - BERT (Bidirectional Encoder Representations from Transformers)

3. **Feature Engineering**:
   - TF-IDF vectorization
   - Word embeddings
   - Text preprocessing and cleaning
  
## Dataset

This dataset is a collection of datasets from different sources related to the automatic detection of cyber-bullying.
The data is from different social media platforms like Kaggle, Twitter, Wikipedia Talk pages, and YouTube. The data contains text and 
are labeled as bullying or not. The data contains different types of cyber-bullying like hate speech, aggression, insults, and toxicity.
You have been provided with the twitter_parsed tweets dataset, wherein you have to classify whether the tweet is toxic or not.

### Data Characteristics:

- Social media text data (likely from platforms like Twitter, Facebook, etc.)
- Annotated with cyberbullying categories
- Requires extensive text preprocessing for social media language (slang, emojis, hashtags, etc.)

### Key Challenges Addressed:

1. **Class Imbalance**: Cyberbullying instances are typically rare compared to normal content
2. **Context Understanding**: Cyberbullying often relies on context and subtle language cues
3. **Noisy Text Data**: Social media text contains informal language, abbreviations, and emojis
4. **Multiple Languages**: Need to handle different linguistic patterns and cultural contexts

### Evaluation Metrics:
- Accuracy
- Precision and Recall (particularly important due to class imbalance)
- F1-score
- Confusion Matrix analysis

This is a critical real-world application of NLP that addresses the growing concern of online harassment and aims to create safer digital spaces through automated content moderation systems.

