```python
from django.db import models


class AIModel(models.Model):
    emotional_intelligence = models.BooleanField(default=False)
    contextual_awareness = models.BooleanField(default=False)
    transfer_learning = models.BooleanField(default=False)
    reinforcement_learning = models.BooleanField(default=False)
    advanced_nlp_nlu = models.BooleanField(default=False)
    advanced_nlg = models.BooleanField(default=False)
    speech_synthesis_recognition = models.BooleanField(default=False)
    reasoning = models.BooleanField(default=False)
    self_reflection = models.BooleanField(default=False)
    customizable = models.BooleanField(default=False)
```
