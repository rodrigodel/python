import openai
from my_key_chat_gpt import api_key

openai.api_key = api_key

consulta = input('Consulta: ')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=consulta,
  temperature=0.3,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#print(response)
resultado = (response['choices'][0]['text'])
print(resultado)
