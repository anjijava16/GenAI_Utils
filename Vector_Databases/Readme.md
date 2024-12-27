# A Quick History of Embeddings

Embeddings have transformed language processing, evolving dramatically over the years:

1. Word2Vec (2013): This model introduced the concept of word embeddings. It used two methods:

2. Skip-Gram: Predicts nearby words from a given word. For example, in "The cat sat on the mat," knowing "cat" helps predict words like "sat" and "mat."

3. Continuous Bag of Words (CBOW): Predicts a word based on its surrounding context. Here, "The," "sat," and "on" help predict "cat."

3. Word2Vec created spaces where words with similar meanings (e.g., "cat" and "dog") were placed close together.


GloVe (2014): Short for Global Vectors for Word Representation, GloVe improved on Word2Vec by analyzing how often words co-occur across a dataset. This method revealed deeper relationships, such as the famous "king - man + woman = queen" analogy.

Transformers (2018): Models like BERT and GPT took embeddings further by focusing on context. Unlike earlier static embeddings, transformers adapt to how words are used in a sentence. For instance, "bank" in "river bank" and "financial bank" gets distinct representations.


These advances made it possible for AI to capture the intricacies of human language with remarkable accuracy.

🔢 Embedding Language at Every Level

Embeddings aren’t limited to words. They can represent sentences, paragraphs, or even entire documents. This flexibility is key for applications ranging from search engines to chatbots.

# Why Embed Different Sizes?

1. Word Embeddings: Great for tasks requiring precise word relationships, like finding synonyms.

2. Sentence Embeddings: Capture the overall meaning of a sentence. Useful for tasks like question answering.

3. Paragraph or Document Embeddings: Capture broader themes, essential for summarization or categorization.
