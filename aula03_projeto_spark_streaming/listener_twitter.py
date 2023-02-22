import socket
import tweepy

HOST = 'localhost'
PORT = 9009
s = socket.socket()
s.bind((HOST, PORT))
print(f"Aguardando conexão na porta: {PORT}")

s.listen(5)
connection, address = s.accept()
print(f"Recebendo solicitação de {address}")

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAEWIUAEAAAAAU49qkkegQd58kO0B%2FIB77iclVLg%3DUFuFnFZiMhocJdBIZQ1n7ygcqE8l4CeXvpMuzjZPziMWY5jhaE'
keyword = 'política'

class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print("="*50)
        connection.send(tweet.text.encode('utf-8', 'ignore'))

printer = GetTweets(BEARER_TOKEN)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()


connection.close()