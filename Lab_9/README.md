### Installation Instructions

Follow these steps to set up the required dependencies:

1. Install the necessary libraries:
    ```bash
    pip install nltk spacy numpy hmmlearn scikit-learn
    ```

2. Download `spacy` language models:
    ```bash
    python -m spacy download en_core_web_sm
    python -m spacy download de_core_news_sm
    ```

3. Download required `nltk` data:
    ```python
    import nltk
    nltk.download("punkt_tab")
    nltk.download("averaged_perceptron_tagger_eng")
    ```
