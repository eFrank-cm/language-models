import openai

with open('token_api.txt') as f: token = f.read()

openai.api_key = token

while True:
    prompt = input("\n>> ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=2048)

    print(completion.choices[0].text)
