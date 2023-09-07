import re

def print_summary(userAnswers):
    print("\nResumen de respuestas:")
    for key, value in sorted(userAnswers.items()):
        print(f"{key}: {value}")

def validate_answer(answer, regex):
    return re.fullmatch(regex, answer) is not None

def ask_questions(questions):
    answers = {}
    for question in questions:
        while True:
            if question["type"] == "select":
                for i, option in enumerate(question["options"], 1):
                    print(f"{i}. {option}")

            response = input(question["label"]).strip()

            if validate_answer(response, question["validation"]):
                if question["type"] == "amount":
                    answers[question["id"]] = float(response)
                elif question["type"] == "boolean":
                    answers[question["id"]] = True if response.lower() == 'si' else False
                elif question["type"] == "select":
                    answers[question["id"]] = question["options"][int(response) - 1]
                break
            else:
                print(f"Entrada inválida. {question['indications']}")
    # print_summary(answers)
    return answers
