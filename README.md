# CustomEmailAI

Integration between Jellyfin, Gmail, OpenAI, DeepAI for Personalized Movie Recommendations

## Overview

This tool integrates multiple APIs to create custom movie recommendations. It searches all movies stored in Jellyfin, selects a random one, and uses OpenAI to prepare a prompt. The prepared prompt is then used in DeeAI to generate an image of your cat participating in the selected movie.

The script also creates a story based on your cat recommending the movie and describing its experience participating in it.

## Requirements

* Runs from `Application.py`
* Requires API keys for OpenAI, DeepAI, and Gmail configured in a safe `.ENV` file
* Uses Ubuntu batch scripts to search movies stored in Jellyfin

## Workflow

1. **Movie Selection**: The script runs `readmovies.selectMovie(1)`, which searches all current movies using an Ubuntu batch script and selects a random one.
2. **Prompt Preparation**:
        * The output from the previous step is passed to `CustomPrompts.CLoverPrompt(movie)` to prepare prompts for OpenAI.
3. **OpenAI Integration**: The prepared prompt is sent to OpenAI using `CustomPrompts.sendToOpenAI(pre_prompt, openAIkey)`.
4. **DeepAI Integration**:
        * The full prompt from OpenAI is used in DeeAI to generate an image of your cat participating in the selected movie.
        * The generated image is downloaded and saved locally.
5. **Email Preparation**: Finally, a story based on your cat recommending the movie and describing its experience participating in it is prepared.

## Configuration**

API keys for OpenAI, DeepAI, and Gmail must be configured in a safe `.ENV` file to interact with these APIs.

Example output
![alt text](https://github.com/suazojaime/CustomEmailAI/blob/main/cutomEmail.png)
