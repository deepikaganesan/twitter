from flask import Flask, render_template, request
import tweepy
consumer_key = "klc9lTZuJfxAalGGOIXFjTbhr"
consumer_secret = "gPhGZE1j6egZSXTkyw5p3mZdem2VhNb8aHxfCae7PtPggJKF8q"
access_token = "1112587571622637568-BR4xHHlqA7L0e58zp0bKB9U6I5AFfj"
access_token_secret = "GrcusxoUGerHchMsbmdTFRw6ZHbnCcI7NTa85GL2LjDLu"
app=Flask(__name__)
@app.route('/')
def index():
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  search=request.args.get('query')
  public_tweets = api.user_timeline(search,count=10)
  return render_template('ho.html', tweets=public_tweets)
if __name__=='__main__':
  app.run(debug=True)


<!DOCTYPE html>
<html>
<head>
	<title>Flask Tutorial</title>
	<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css">
</head>
<body>
<div class="container">
 <div class="row justify-content-center">
   <div class="col-md-6">
     <div class="p-5">
       <form class="form-inline" method="GET" action="{{ url_for('index') }}">
	 <input class="form-control" type="text" name="query">
	 <button class="btn btn-primary" type="submit">search</button>
       </form>
     </div>
	  {% for tweet in tweets %}
	  <div class="card mt-2">
	    <div class="card-body">
	      <div class="card-text">
		  {{ tweet._json.text }}
	      </div>
            </div>
	  </div>
	  {% endfor %}
       </div>
   </div>
 </div>
</body>
</html>  
        
