# nokia-ai-chatbot

A simple AI chatbot built using Python, TF-IDF, and cosine similarity.  
This project demonstrates how a basic information-retrieval chatbot can be implemented using classical NLP techniques without deep learning.

It was developed as a mini project for AI Automation Intern applications, such as Nokia Turkey R&D.

---

## Features

- Text preprocessing (lowercasing and cleaning)
- TF-IDF vectorization
- Cosine similarity for answer matching
- FAQ-style question-answering
- Simple terminal interface
- Lightweight and fully local execution

---

## Project Structure

nokia-ai-chatbot/
│
├── chatbot.py        # Chatbot logic (TF-IDF and similarity search)
└── README.md         # Project documentation

---

## How It Works

1. The chatbot loads an internal FAQ dataset defined in the code.
2. Each FAQ question is converted into a numerical representation using TF-IDF.
3. User input is also vectorized with the same TF-IDF model.
4. Cosine similarity is used to find the closest matching FAQ question.
5. The corresponding answer is returned. If similarity is too low, the chatbot responds with: "I'm still learning."

This reflects a classical information retrieval chatbot often used in early automation and customer-support systems.

---

## Installation

Install required Python packages:

pip3 install scikit-learn  
pip3 install scipy  

---

## Running the Chatbot

Execute the chatbot from the terminal:

python3 chatbot.py  

Expected startup screen:

Nokia-style AI Automation Chatbot  
Type your question (or 'quit' to exit).  
--------------------------------------------------  
You:

---

## Example Interaction

You: What is network automation?  
Bot: Network automation means using software to configure, monitor and manage network devices automatically.

---

## Purpose of the Project

This project demonstrates:

- Basics of classical NLP
- TF-IDF vectorization
- Cosine similarity for query matching
- Basic automation logic in Python
- Ability to build functional prototypes for real-world use cases

Suitable for:

- AI Automation Intern
- Software Engineering Intern
- Machine Learning Intern

---

## Technologies Used

- Python 3
- scikit-learn
- NumPy
- Terminal interface

---

## Author

Elif Aydın  
GitHub: https://github.com/elfynme22

---

## License

This project is open-source for educational and demonstration purposes.
