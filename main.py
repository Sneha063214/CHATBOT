
from flask import Flask,request,jsonify,send_from_directory
app=Flask(__name__)
import pandas as pd



def get_responsee():
    print("Chatbot: Hi!I'm your simple chatbot.Type 'bye' to exit ")

    while(True):
        user_input=input("You: ").lower()

        if(user_input=="bye"):
            print("Chatbot: Goodbye!Have a nice day 😊")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I am fine . What about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple Chatbot")
        
        elif "help" in user_input:
            print("Chatbot: I can chat with you.Try saying something else")
        else:
            print("Chatbot: Sorry I don't understand that")
#run the chatbot
# get_response()


# @app.route("/")
# def home():
#      return send_from_directory('.','forms.html')

# @app.route("/chat",methods=["POST"])
 
# def chat():
#      data=request.json
#      user_message=data.get("message")
#      response = get_response(user_message)
#      return jsonify({"response":response})

# if __name__=="__main__":
#      print("chatbot is running ! visit http://127.0.0.1:5500/forms.html in your browser")
#      print("server test.html file")
#      app.run(debug=True)
     









    









