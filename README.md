# Python Thai Sentiment Analysis (PyThaiSA)

[![Build Status](https://travis-ci.org/PyThaiNLP/thai-sentiment-analysis.svg?branch=master)](https://travis-ci.org/PyThaiNLP/thai-sentiment-analysis)
[![Coverage Status](https://coveralls.io/repos/github/PyThaiNLP/thai-sentiment-analysis/badge.svg?branch=master)](https://coveralls.io/github/PyThaiNLP/thai-sentiment-analysis?branch=master)


Python Thai sentiment analysis **(For Dev only)**

## Install

```
$ pip install https://github.com/PyThaiNLP/thai_sentiment_analysis/archive/master.zip
```

## Use

Google Colab : https://colab.research.google.com/drive/17y4tc69O6Z-dr1LbgR5FlPYZK46xCKbY

```python
from pythaisa import *
datatrain=[("ฉันรักคุณ","love"),("ผมก็รักคุณเหมือนกัน","love"),("เกลียดคุณ","neg"),("เกลียดเหมือนกัน","neg")]
m=model(name="test",train_dataset=datatrain)
m.train()
print(m.predict("ฉันรักคุณ"))
```

