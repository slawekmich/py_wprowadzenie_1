import os
import openai

openai.api_key = ("sk-OAR76F88FQ6ywLOT5cGW##T3BlbkFJXnF5t8Bu23O25LlhMurd")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Correct this to standard English:\n\nShe no went to the market.",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
