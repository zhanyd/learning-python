from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="A man in the ruins of war, wearing modern combat uniform, cyberpunk style",
  n=1,
  size="1024x1024",
  quality="standard"
)

print(response)