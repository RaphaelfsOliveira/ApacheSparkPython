import socket
import tweepy

HOST = '127.0.0.1'
PORT = 9009
KEYWORD = 'economia' # verificar api twitter depois

s = socket.socket()
s.bind((HOST, PORT))
print(f"Aguardando conexão na porta: {PORT}")

s.listen(5)
connection, address = s.accept()
print(f"Recebendo solicitação de {address}")

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAEWIUAEAAAAAU49qkkegQd58kO0B%2FIB77iclVLg%3DUFuFnFZiMhocJdBIZQ1n7ygcqE8l4CeXvpMuzjZPziMWY5jhaE'

class GetTweets(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(tweet.text)
        print("=" * 50)
        connection.send(tweet.text.encode('utf-8', 'ignore'))

client = GetTweets(BEARER_TOKEN)
client.add_rules(tweepy.StreamRule(KEYWORD))
client.filter()


connection.close()