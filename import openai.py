import os
import openai

openai.api_key = os.getenv("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")
# openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="# Python 3 \ndef remove_common_prefix(x, prefix, ws_prefix): \n    x[\"completion\"] = x[\"completion\"].str[len(prefix) :] \n    if ws_prefix: \n        # keep the single whitespace as prefix \n        x[\"completion\"] = \" \" + x[\"completion\"] \nreturn x \n\n# Explanation of what the code does\n\n#",
  temperature=0,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)