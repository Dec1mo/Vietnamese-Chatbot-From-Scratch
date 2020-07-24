<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/FxL5qM0.jpg" alt="Bot logo"></a>
</p>

<h3 align="center">Vietnamese Drink Ordering Chatbot</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-inactive-red)]()
  [![Platform](https://img.shields.io/badge/platform-Messenger-blue.svg)]()
  [![Built-in_NLP](https://img.shields.io/badge/Facebook_Built--in_NLP-ON-brightgreen.svg)]()

</div>

---

<p align="center"> 🤖 A Messenger chatbot built without any frameworks which able to chat, send stickers, provide information, help users order drinks and pay. 
    <br> 
</p>

## 📝 Table of Contents
+ [About](#about)
+ [Demo](#demo)
+ [How it works](#working)
+ [Getting Started](#getting_started)

## 🧐 About <a name = "about"></a>
Vietnamese Drink Ordering Chatbot = Intent classification + Context + (Address fuzzy matching + Facebook Built-in NLP)

## 🎥 Demo <a name = "demo"></a>
![Working](https://media.giphy.com/media/LOc3MaQ9sh72gScetp/giphy.gif)

## 💭 How it works <a name = "working"></a>
A session starts with a message from a user.

When the bot receives a text message, it predicts the intent (greeting, goodbye, complain, praise, thanks, sorry, ask_drink, order, ask_coupon, payment, ask_owner) of the text.
If it is:
+ ask_drink/order: The bot responses a template for user to pick his drink and topping.
+ ask_payment: The bot sets up a context, asks and stores user's information that required for delivery order such as: phone number, time of receipt, location. 
  + The bot uses Built-in NLP of Facebook to get phone number and time of receipt effectively and accurately.
  + The bot uses fuzzy matching to match the input location with a location in a standard address table to parse the input location.

## 🏁 Getting Started <a name = "getting_started"></a>
### Requirements
+ [Facebook Messenger app](https://developers.facebook.com/)
+ [ngrok](https://ngrok.com/) - An awesome and easy tool which creates a secure tunnel on your local machine along with a public URL. I used a json file instead of a database but you can use [Heroku](https://www.heroku.com/) instead of ngrok and json.
+ [underthesea](https://pypi.org/project/underthesea/)
+ [sklearn](https://pypi.org/project/sklearn/)
+ [tensorflow](https://pypi.org/project/tensorflow/)
+ [Keras](https://pypi.org/project/Keras/)
+ [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/)
+ [bottle](https://pypi.org/project/bottle/)

### Installing
#### Train and save the intent classification model
```
>> python model/model.py
```
#### Crawl [the real drink data](https://loship.vn/trasuachain)
```
>> python crawler/data_crawler.py
```
#### Generate an Access Token for your page
<a href="" rel="noopener">
 <img src="https://i.imgur.com/cbsv60v.png" alt="access_token"></a>

#### Put the token we had just generated into server.py file
```python
PAGE_TOKEN = "EAAQgL..."
```
#### Run server on localhost
```
>> python server/server.py
```
#### Run ngrok, remember to use the same port as the port localhost holding
```
>> ngrok.exe http 8088
```
You will get something like this:
<a href="" rel="noopener">
 <img src="https://i.imgur.com/ZlVRPtq.png" alt="ngrok"></a>

#### Create a webhook, using Callback URL as https URL in ngrok console and Verify Token as access Token, we have just generated
<a href="" rel="noopener">
 <img src="https://i.imgur.com/in9Dwbd.png" alt="webhooks"></a>

#### Remember to turn on Built-in NLP and set up Default Language Model
<a href="" rel="noopener">
 <img src="https://i.imgur.com/wfjukqW.png" alt="built-in_NLP"></a>

Now your Messenger Chatbot is ready to chat with you!
