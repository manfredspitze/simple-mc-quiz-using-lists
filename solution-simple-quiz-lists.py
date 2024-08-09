def quiz():
    # List of questions
    questions = [
        "What is the capital of France?",
        "What is 2 + 2?",
        "What is the largest planet in our solar system?",
        "What is the chemical symbol for water?",
        "Who wrote 'Romeo and Juliet'?"
    ]

    # List of possible answers
    options = [
        ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        ["A) 3", "B) 4", "C) 5", "D) 6"],
        ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        ["A) H2O", "B) CO2", "C) O2", "D) H2"],
        ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"]
    ]

    # List of correct answers
    correct_answers = ["A", "B", "C", "A", "B"]

    # Initialize score
    score = 0

    # Loop through each question
    for i in range(len(questions)):
        print(f"Question {i + 1}: {questions[i]}")
        for option in options[i]:
            print(option)
        
       
        answer = input("Your answer (A, B, C, or D): ").strip().upper()

      
        if answer == correct_answers[i]:
            print("Correct!\n")
            score += 2
        else:
            print("Incorrect.\n")

    # Display final score
    print(f"Your final score: {score} out of {len(questions) * 2}")
    print(f'Percent correct: {score / ( len(questions) * 2) * 100:.2f}%')

quiz()
