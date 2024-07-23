# # # from aleph_alpha_client import AlephAlphaClient
# # #
# # # # Replace 'YOUR_API_KEY' and 'YOUR_API_HOST' with your actual API key and host URL
# # # api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJ0b2tlbl9pZCI6MjR9.XJUgadoAEH8LhsDpI6wdHGj-JftK6UN2v_wa662Z90A'
# # # api_host = 'http://20.190.193.161:8000'
# # #
# # # # Initialize the Aleph Alpha client with your custom host
# # # client = AlephAlphaClient(api_key, host=api_host)
# # #
# # # # Example: Make a call to the 'generate' API endpoint
# # # text = "Once upon a time, in a land far, far away..."
# # # response = client.generate(text)
# # #
# # # # Print the generated text
# # # print(response['text'])
# # #
# #
# # import os
# # from aleph_alpha_client import Client, CompletionRequest, Prompt
# #
# # client = Client(host='http://20.190.193.161:8000', token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJ0b2tlbl9pZCI6MjR9.XJUgadoAEH8LhsDpI6wdHGj-JftK6UN2v_wa662Z90A')
# # request = CompletionRequest(
# #     prompt=Prompt.from_text("Provide a short description of AI:"),
# #     maximum_tokens=64,
# # )
# #
# # print('-----------------------------------')
# # response = client.complete(request, model="luminous-extended")
# # print('---------2--------------------------')
# #
# # print(response.completions[0].completion)

# import os
# import openai

# openai.api_type = "azure"
# # openai.api_base = "http://localhost:8080"
# openai.api_base = "https://hpe-genai.openai.azure.com/"
# openai.api_version = "2023-07-01-preview"
# openai.api_key = "9732f6fe884f461592b1b2033a842732"
# # openai.api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ3YXFhci5oYXNzYW5AaHBlLmNvbSIsInF1b3RhSWQiOiI4ZTVjNjRlNi1kYzhmLTQ0MjAtOGQ5ZS1lMDQ2OTYyOWJhNTMiLCJpc3MiOiJsb2NhbGhvc3Q6OTAwMCIsImV4cCI6MTcxODU2MjcwNywiaWF0IjoxNzEwNzkwMzA5LCJqdGkiOiIxY2U5MjljYi05YTYxLTQwZGUtOTQ5ZC1mZDY1NWIxNmVkMDgiLCJ3b3Jrc3BhY2VJZCI6IjUzMGMzYmFjODU4ZTExZWVhMmZjMzY2MWE4YmFiNWE1In0.raaqcE26lLCmASqfUPvlwjeRyIJTxptmCzMUTtjYfbs"

# messages = [
#     {
#         "role": "user",
#         "content": "tell me a joke"
#     },
#     {
#         "role": "system",
#         "content": "give instructions,,,"
#     }
# ]
# response = openai.ChatCompletion.create(
#     # model="GPT-3.5-Turbo",
#     engine=  "glp-genai-gpt3",
#     # engine="HPE",
#     messages=messages,
#     temperature=0.7,
#     max_tokens=800,
#     top_p=0.95,
#     frequency_penalty=0,
#     presence_penalty=0,
#     stop=None)

# print(response)



import openai
from openai import AzureOpenAI

client = AzureOpenAI(
  api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ3YXFhci5oYXNzYW5AaHBlLmNvbSIsInF1b3RhSWQiOiIiLCJpc3MiOiJldGhhbi1kZXYuY2NwLmV0aGlhbi5xYS5ocGVzYW5kYm94Lm5ldCIsImV4cCI6MTcyNTg3NDMwOSwiaWF0IjoxNzE4MDk4MzEwLCJqdGkiOiIxMjk3YzEwMi00NWRlLTQwODMtYTA4OS05MTVmYjAxOWQzYWQiLCJ3b3Jrc3BhY2VJZCI6IjcwZDA2MDUyZjY2MTExZWViMjJjOTJkMzFlOGE1ZDk1In0.V9dec_Gy15-AnOwr4QuQD1YhyzNF2wTTO-h-234NgJU",
  api_version="2023-07-01-preview", 
  base_url="https://ethan-dev.ccp.ethian.qa.hpesandbox.net/proxy")

# openai.api_key = "9732f6fe884f461592b1b2033a842732"
# TODO: The 'openai.base_url' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(base_url="https://ethan-dev.ccp.ethian.qa.hpesandbox.net/proxy")'
# openai.base_url = "https://ethan-dev.ccp.ethian.qa.hpesandbox.net/proxy"

messages = [
    {"role": "user", "content": "tell me something productive"},
]
response = client.chat.completions.create(model="Azure OpenAI GPT 3.5",
messages=messages,
temperature=0.7,
max_tokens=800,
top_p=0.95,
frequency_penalty=0,
presence_penalty=0,
stop=None)

# Print the generated text
print(response.text)