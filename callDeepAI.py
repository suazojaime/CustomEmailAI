import requests
import wget

def callAI(message, key):
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': message,
            },
        headers={'api-key': key}
        )
    response = r.json()

    wget.download(response['share_url'], out='/home/tambor/recomendations/clover/photoBomb.jpg')
    
    return(response)
    
    
