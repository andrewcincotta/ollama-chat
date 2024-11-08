import subprocess as sp
import requests


def findModels():
    ollOutput = sp.check_output(['ollama', 'list']).decode('utf-8')

    lines = ollOutput.split('\n')[1:]

    models = []
    for line in lines:
        if line.split():
            models.append(line.split()[0])

    return models


def printModels(models):
    print('List of models installed by ollama:')

    for index, model in enumerate(models):
        print(index + 1, ". ", model)


def chatWithGranite(prompt, model):
    response = requests.post('http://localhost:11434/api/generate',
                             json={
                                 'model': model,
                                 'prompt': prompt,
                                 'stream': False
                             })
    return response.json()['response']


if __name__ == "__main__":
    models = findModels()

    printModels(models)

    modelIndex = int(input("Enter # of model you want to use: "))
    modelIndex -= 1

    while True:
        userInput = input("You: ")
        if userInput.lower() in ['quit', 'exit']:
            break
        else:
            response = chatWithGranite(userInput, models[modelIndex])
            print("\nAI: ", response)
