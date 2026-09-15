def run_quiz(question):
    score=0
    for i,q in enumerate(question):
        print(f"\n Question{i+1}:{q['question']}")
        for option in q['options']:
            print(option)
        ans=input("Enter your answer:").strip().upper()
        if ans== q['ans']:
            print('correct')  
            score+=1
        else:
            print(f"wrong!!! \n Right answer is {q['ans']}")
    print (f"You got {score} out of {len(question)}")          

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Rome"],
        "ans": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "ans": "B"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["A. J.K. Rowling", "B. Jane Austen", "C. Charles Dickens", "D. Mark Twain"],
        "ans": "A"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. H2O", "B. CO2", "C. O2", "D. NaCl"],
        "ans": "A"
    },
    {
        "question": "Who was India's captain during the ICC T20 World Cup 2024?",
        "options": ["A. Hardik Pandya", "B. Rohit Sharma", "C. KL Rahul", "D. Virat Kohli"],
        "ans": "B"
    },
    {
        "question": "Which Indian player won the Player of the Tournament in T20 World Cup 2024?",
        "options": ["A. Jasprit Bumrah", "B. Virat Kohli", "C. Suryakumar Yadav", "D. Arshdeep Singh"],
        "ans": "A"
    },
    {
        "question": "Who was the top run-scorer for India in IPL 2024?",
        "options": ["A. Shubman Gill", "B. Virat Kohli", "C. Ruturaj Gaikwad", "D. Sanju Samson"],
        "ans": "B"
    },
    {
        "question": "Which team won IPL 2024?",
        "options": ["A. Mumbai Indians", "B. Chennai Super Kings", "C. Kolkata Knight Riders", "D. Gujarat Titans"],
        "ans": "C"
    },
    {
        "question": "Who took a hat-trick for India against Australia in the ODIs series?",
        "options": ["A. Bumrah", "B. Axar Patel", "C. Arshdeep Singh", "D. Kuldeep Yadav"],
        "ans": "D"
    },
    {
        "question": "Who is currently India's head coach (2025)?",
        "options": ["A. Rahul Dravid", "B. VVS Laxman", "C. Anil Kumble", "D. Gautam Gambhir"],
        "ans": "D"
    },
    {
        "question": "Which stadium hosted the T20 World Cup 2024 final?",
        "options": ["A. Eden Gardens", "B. Narendra Modi Stadium", "C. MCG", "D. Kensington Oval"],
        "ans": "D"
    },
    {
        "question": "Which Indian bowler reached 100 T20I wickets in 2024?",
        "options": ["A. Bhuvneshwar Kumar", "B. Ravindra Jadeja", "C. Yuzvendra Chahal", "D. Jasprit Bumrah"],
        "ans": "D"
    },
    {
        "question": "Which young Indian player made his debut in 2024 and impressed in T20s?",
        "options": ["A. Riyan Parag", "B. Tilak Varma", "C. Yashasvi Jaiswal", "D. Abhishek Sharma"],
        "ans": "D"
    }
]

print("📚 Welcome to the Quiz Game!")
run_quiz(quiz_questions)
