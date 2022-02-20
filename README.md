## Purpose

Used to analyze how speech recognition models - like AWS Transcribe - may misinterpret women and people of color. Then tested with a sentiment analysis tool.

## How to use

1. Install dependences

```
    python -m pip install -U pip
    python -m pip install -U matplotlib
    pip install -U textblob
    python -m textblob.download_corpora
```

2. Run sentimenttest.py to view graphs of sentiment tools compared to Standfords dataset
3. Run analyzeSentiment.py to test the all files within awsData and transcribedData to generate results within analyzedAwsData and analyzedTranscribedData
