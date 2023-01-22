import urllib.request
import os
import openai
from __api_key_ import *
openai.organization = orgkey
openai.api_key = apikey
image_description = input("image description for generate :")
st=openai.Image.create(
    prompt=image_description,
  n=3,
  size="512x512"
)
list_image=st.get("data")

for img in list_image:
    print(img.get("url"),None)
   
