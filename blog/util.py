import requests
from celery import shared_task
from easy_thumbnails.files import generate_all_aliases
import re


@shared_task
def generate_responsive_images(post):
    generate_all_aliases(post.image, True)
    post.image_resized = True
    post.save()


def find_hashtags(text):

    pattern = re.compile(r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)')
    users = pattern.findall(text)
    return users


@shared_task
def send_mail(mailOptions):

    response = requests.post('http://127.0.0.1:3000/api', data=mailOptions)

    if response.status_code != 200:
        print('Huvo un error al enviar el mail')
    else:
        print("WIIIIIIII se envio el correo")
