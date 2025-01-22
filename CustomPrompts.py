from openai import OpenAI

def CLoverPrompt(movieList):
    message = f''' Create a very short description of a majestic black cat with an abundance of fur. The cat should have distinctive white stripes on its chest, neck, and paws,
    describe it participating in the movie {movieList[0]}, do not name the cat '''
    return message

def CLoverHistory(movieList):
    message = f''' Create a very short story in spanish of our cat Cloverfield recomending us to see the movies ( {movieList[0]} ),
he shares his experience about filming and leading the movie, with a latin chilean slang and expressions
return html tags with css to give it color and shape
return only the html tags and content, no explanation or introduction, the response must strictly start with <html> with no other characters afteer that ,no ticks or quotes'''
    return message


def sendToOpenAI(message, key):
    client = OpenAI(api_key=key)
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": message,
            }],
        model="gpt-4-1106-preview",)
    query_cost_USD = float(chat_completion.usage.total_tokens) * 0.01/1000.0
    query_cost_CLP = query_cost_USD*900.0
    cloverMessage = chat_completion.choices[0].message.content    

    return([query_cost_USD, query_cost_CLP, cloverMessage])
