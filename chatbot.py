from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

FAQ_QUESTIONS = [
    "What is network automation?",
    "What does an AI automation intern do?",
    "What programming languages are useful at Nokia?",
    "What is a large language model?",
    "What is log analysis?",
    "What is RAG in AI?",
    "What is the benefit of using Python in automation?"
]

FAQ_ANSWERS = [
    "Network automation means using software to configure, monitor and manage network devices automatically.",
    "An AI automation intern helps build scripts, tools and chatbots that automate repetitive tasks and analyze data.",
    "At Nokia, Python is useful for automation. Java, C++ and web technologies are also important depending on the team.",
    "A large language model is an AI system trained on huge amounts of text so it can understand and generate human-like language.",
    "Log analysis means reading and processing system logs to detect errors, patterns or performance issues.",
    "RAG (Retrieval-Augmented Generation) retrieves relevant documents first, then generates an answer based on them.",
    "Python is popular for automation because it's simple, fast to write and has strong data processing libraries."
]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(FAQ_QUESTIONS)

def find_best_answer(user_question):
    user_vec = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vec, faq_vectors)[0]
    best_index = similarities.argmax()
    best_score = similarities[best_index]

    if best_score < 0.1:
        return "I'm not sure about that yet, but I'm still learning."
    return FAQ_ANSWERS[best_index]

def main():
    print("Nokia-style AI Automation Chatbot")
    print("Type your question (or 'quit' to exit).")
    print("-" * 50)

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "exit", "bye", "q"]:
            print("Bot: Goodbye!")
            break
        answer = find_best_answer(user_input)
        print("Bot:", answer)
        print()

if __name__ == "__main__":
    main()
