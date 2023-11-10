from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="A Iron Man fly into the sky",
  n=1,
  size="1024x1024",
  quality="standard"
)

print(response)