import random

def greet_user():
    greetings = [
        "Hello! I'm your Study Help Assistant. How can I support you today?",
        "Hi there, future engineer! What do you need help with?",
        "Welcome! Ready to boost your study game?"
    ]
    print(random.choice(greetings))

def provide_help(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "greeting" in user_input:
        return "Hello! How can I help you today?"

    elif "goodbye" in user_input or "bye" in user_input or "see you" in user_input:
        return "Goodbye! Stay focused and keep learning."

    elif "syllabus" in user_input:
        return "You can download your syllabus from your university's official website or your department portal."

    elif "subjects" in user_input:
        return "Typical B.Tech subjects include Data Structures, Operating Systems, DBMS, Computer Networks, and Software Engineering."

    elif "study tips" in user_input or "study plan" in user_input:
        return "Best tip: Make a daily schedule, set clear goals, revise regularly, and practice coding problems on platforms like LeetCode or GeeksforGeeks."

    elif "motivation" in user_input or "quote" in user_input:
        quotes = [
            "Believe you can, and you're halfway there.",
            "Push yourself, because no one else is going to do it for you.",
            "Your future is created by what you do today, not tomorrow."
        ]
        return random.choice(quotes)

    # Generative AI related questions
    elif "what is generative ai" in user_input or "define generative ai" in user_input:
        return "Generative AI is a type of AI that can create new content such as text, images, code, or music by learning patterns from data."

    elif "uses of generative ai" in user_input or "applications of generative ai" in user_input:
        return "Generative AI is used in content creation, coding assistance, virtual assistants, image generation, video editing, and game development."

    elif "examples of generative ai" in user_input or "generative ai tools" in user_input:
        return "Popular tools include ChatGPT, DALL·E, Midjourney, Stable Diffusion, and GitHub Copilot."

    elif "impact of generative ai" in user_input or "jobs" in user_input:
        return "Generative AI may automate some tasks but creates new opportunities in AI development, model training, ethics, and prompt engineering."

    elif "ai in education" in user_input or "generative ai in education" in user_input:
        return "Generative AI helps students by summarizing notes, generating practice questions, offering explanations, and creating study plans."

    # New student help topics
    elif "internship" in user_input:
        return "Look for internships on platforms like Internshala, LinkedIn, or company career pages. Build a solid resume and highlight your projects."

    elif "resume" in user_input or "cv" in user_input:
        return "A good resume includes a strong objective, your education, key projects, technical skills, and internship experience. Keep it to one page."

    elif "project idea" in user_input or "mini project" in user_input:
        return "Some cool ideas: Student Attendance System using Face Recognition, Chatbot using NLP, Portfolio Website, or IoT-based Home Automation."

    elif "time management" in user_input:
        return "Use the Pomodoro technique (25-min study, 5-min break), plan daily tasks, avoid multitasking, and prioritize important work first."

    elif "exam preparation" in user_input or "prepare for exam" in user_input:
        return "Revise key topics first, solve previous year papers, make short notes, avoid cramming, and stay consistent with a daily study schedule."

    # Help or menu command
    elif "help" in user_input or "menu" in user_input:
        return (
            "Here are some things you can ask me:\n"
            "• Syllabus info — 'What's in the syllabus?'\n"
            "• Subjects — 'What are core B.Tech subjects?'\n"
            "• Study tips — 'How do I make a study plan?'\n"
            "• Motivation — 'Give me a motivational quote'\n"
            "• Generative AI — 'What is Generative AI?'\n"
            "• Internships — 'How do I find an internship?'\n"
            "• Resume help — 'How to make a good resume?'\n"
            "• Project ideas — 'Suggest some mini projects'\n"
            "• Time management — 'How do I manage time?'\n"
            "• Exam tips — 'How do I prepare for exams?'\n"
            "• Type 'exit' or 'quit' to end the chat."
        )

    elif "exit" in user_input or "quit" in user_input:
        return "exit"

    else:
        return "Sorry, I don't have information on that yet. Try asking about syllabus, subjects, study tips, motivation, or Generative AI topics."

def chatbot():
    greet_user()
    while True:
        user_input = input("\nYou: ")
        response = provide_help(user_input)
        if response == "exit":
            print("Goodbye! Stay focused and keep learning.")
            break
        else:
            print("\nAssistant:", response)

if __name__ == "__main__":
    chatbot()
