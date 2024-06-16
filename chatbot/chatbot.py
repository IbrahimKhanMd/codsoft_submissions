import re
import long_responses as long_resp

def msg_prob(user_msg, recog_words, single_resp=False, req_words=[]):
    msg_certainty = 0
    has_req_words = True

    for word in user_msg:
        if word in recog_words:
            msg_certainty =msg_certainty+1

    percentage = float(msg_certainty) / float(len(recog_words))

    for word in req_words:
        if word not in user_msg:
            has_req_words = False
            break

    if has_req_words or single_resp:
        return int(percentage * 100)
    else:
        return 0

def check_msgs(message):
    highest_prob = {}

    def resp(bot_resp, word_list, single_resp=False, req_words=[]):
        nonlocal highest_prob
        highest_prob[bot_resp] = msg_prob(message, word_list, single_resp, req_words)

    resp('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_resp=True)
    resp('See you!', ['bye', 'goodbye'], single_resp=True)
    resp('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], req_words=['how'])
    resp('You\'re welcome!', ['thank', 'thanks'], single_resp=True)
    resp('Thank you!', ['i', 'love', 'code', 'palace'], req_words=['code', 'palace'])

    resp(long_resp.R_ADVICE, ['give', 'advice'], req_words=['advice'])
    resp(long_resp.R_EATING, ['what', 'you', 'eat'], req_words=['you', 'eat'])

    best_match = max(highest_prob, key=highest_prob.get)
    return long_resp.unknown() if highest_prob[best_match] < 1 else best_match

def get_resp(user_input):
    split_msg = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_msgs(split_msg)
    return response

while True:
    print('Bot: ' + get_resp(input('You: ')))
