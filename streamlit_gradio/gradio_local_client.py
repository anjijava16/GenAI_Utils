# pip install gradio_client

from gradio_client import Client

client = Client("https://7cdaf82e3cfbae7b67.gradio.live/")
result = client.predict(
		query="Hello!!",
		api_name="/predict"
)
print(result)
