# Quiz Game

questions = {
    "What is the capital of India?": "delhi",
    "Which language is used for AI and Machine Learning?": "python",
    "How many days are there in a week?": "7",
    "What is 5 + 5?": "10",
    "Which planet is known as the Red Planet?": "mars"
}

score = 0

print("===== Quiz Game =====")

for question, answer in questions.items():
    user_answer = input(question + " ").lower()

    if user_answer == answer:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌")
        print("Correct answer:", answer)

print("\nQuiz Completed!")
print("Your Score:", score, "/", len(questions))
