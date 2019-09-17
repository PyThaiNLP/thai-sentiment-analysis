# Python Thai Sentiment Analysis (PyThaiSA)
Python Thai sentiment analysis **(For Dev only)**

## Install

```
$ pip install https://github.com/PyThaiNLP/thai_sentiment_analysis/archive/master.zip
```

## Use

```python
from pythaisa import *
datatrain=[("ฉันรักคุณ","love"),("ผมก็รักคุณเหมือนกัน","love"),("เกลียดคุณ","neg"),("เกลียดเหมือนกัน","neg")]
m=model(name="test",train_dataset=datatrain)
m.train()
print(m.predict("ฉันรักคุณ"))
```

