✈️ Flight Chatbot
A simple rule-based chatbot built using Python that helps users with basic flight-related queries such as delays, earliest flights, and ticket booking assistance.

📌 Features


👋 Greets users and responds to basic conversation


⏱️ Finds flights with:


Longest departure delay


Longest arrival delay




🌅 Identifies the earliest morning flight


✅ Suggests flights with on-time departures


🎫 Assists users with ticket booking queries


❌ Handles unknown queries gracefully



🛠️ Technologies Used


Python 


Pandas (for data handling)



📂 Dataset Requirement
This chatbot uses a dataset (flights.csv) which should contain the following columns:


carrier – Airline code


flight – Flight number


dep_delay – Departure delay


arr_delay – Arrival delay


dep_time – Departure time


name – Airline name


Make sure to load and preprocess the dataset before using the chatbot.

🚀 How It Works
The chatbot processes user input using simple keyword-based logic.
Example:
get_response("Which flight has the longest departure delay?")

It searches the dataset using Pandas functions like:


idxmax() → for maximum delay


idxmin() → for earliest time or least delay



💡 Sample Inputs
You can try queries like:


"Hello"


"Help"


"Which flight has the longest departure delay?"


"Which flight has the longest arrival delay?"


"Which flight leaves earliest in the morning?"


"Which flight is on time?"


"Book tickets"


"Bye"



⚙️ Function Overview
get_response(user_input)


Takes user input as a string


Returns chatbot response based on conditions


Uses dataset (df) to fetch flight details



📌 Example Output
You: Which flight has the longest departure delay?
Chatbot: this flight number : AA123


👩‍💻 Author
Sneha Sharma

