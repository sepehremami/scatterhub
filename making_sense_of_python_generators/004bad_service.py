import random

def bad_service_chatbot():
    answers = ["We don't do that",
               "We will get back to you right away",
               "Your call is very important to us",
               "Sorry, my manager is unavailable"]
    yield "Can I help you?"
    s = ''
    while True:
        if s is None:
            break
        s = yield random.choice(answers)