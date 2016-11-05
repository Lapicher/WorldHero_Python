from easy_thumbnails.files import generate_all_aliases


def generate_responsive_images(post):
    generate_all_aliases(post.image, True)
    post.image_resized = True
    post.save()