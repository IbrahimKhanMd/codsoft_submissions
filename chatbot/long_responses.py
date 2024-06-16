import random

R_EATING = "I don't like eating anything because I feed only on data 😁"
R_ADVICE = "If I were you,I would have googled it there👍"

def unknown():
    resp = ['Could You pleas re-phase that?',
                "..........",
                'Sounds almost right',
                "What does that mean?"][random.randrange(4)]
    return resp

    