import requests
API_endpoint = "https://jservice.io/api/clues"
API_query ="value=1000"
API_url = API_endpoint +"?" + API_query


def display_clue(clue):
    clue_category = clue["category"]["title"]
    clue_value = clue["value"]
    clue_question = clue["question"]
    clue_answer = clue["answer"]
    print(f"category: {clue_category}")
    print(f"value: {clue_value}")
    print(f"question: {clue_question}")





# for clue in clues:
    


# def current_score ():
#     print("HELLO")
#     if answer == clue_answer:
#         score += clue_value
#     else:
#         score +=0

# print(score)

# current_score()

def random_clue():
    API_endpoint = "https://jservice.io/api/random"
    API_url = API_endpoint +"?"
    r = requests.get(API_url)
    data = r.json()
    print(data)
    return data[0]

def clue_answer():
    API_endpoint = "https://jservice.io/api/random"
    API_url = API_endpoint +"?"
    r = requests.get(API_url)
    data = r.json()
    print(data)
    return data[0]


