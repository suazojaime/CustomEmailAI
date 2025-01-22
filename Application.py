import readmovies
import CustomPrompts
import callDeepAI
import prepareEmail
import os
from dotenv import load_dotenv, dotenv_values


def runAImodels():
    load_dotenv()

    openAIkey = os.getenv("OPENAI_KEY")
    deepAIkey = os.getenv("DEEPAI_KEY")

    movie = readmovies.selectMovie(1)
    pre_prompt = CustomPrompts.CLoverPrompt(movie)
    prompt_story = CustomPrompts.CLoverHistory(movie)
    prompt = CustomPrompts.sendToOpenAI(pre_prompt,openAIkey)
    story = CustomPrompts.sendToOpenAI(prompt_story,openAIkey)
    response = callDeepAI.callAI(prompt[2],deepAIkey)

    prepareEmail.sendEmail(movie,story)

    return ([movie,pre_prompt,prompt_story,prompt,response, story])

runAImodels()

#def prepareEmail(movie, picture, message):
    
    



#[movie,pre_prompt,prompt,response] = runAImodels()
    
    




    
