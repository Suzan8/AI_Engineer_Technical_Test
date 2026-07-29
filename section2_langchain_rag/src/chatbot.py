from rag_pipeline import ask

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        break

    answer, docs = ask(question)

    print("\nAssistant:")
    print(answer)

