from knowledge_base import college_data

def generate_reply(user_message):
    user_message = user_message.lower()

    sorted_keys = sorted(college_data.keys(), key=len, reverse=True)

    for key in sorted_keys:
        if key in user_message:
            return college_data[key]

    return "Sorry, I don't have information about that."
