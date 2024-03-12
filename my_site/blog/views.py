from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Gautam Diwan",
        "date": date(2023, 2, 28),
        "title": "Travelling",
        "excerpt": "Exploring distant lands, hike majestic mountains, and immerse ourselves in cultural wonders, embracing the serenity of nature's vast landscapes and the thrill of new encounters.",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt placeat nihil quo architecto nostrum mollitia optio! Voluptas, mollitia facilis hic voluptatum nesciunt rem distinctio debitis sapiente molestias, culpa perspiciatis impedit rerum minima minus, labore provident beatae. Aliquam, tenetur nisi mollitia consequuntur ex, quis illo blanditiis maxime optio, possimus atque et.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt placeat nihil quo architecto nostrum mollitia optio! Voluptas, mollitia facilis hic voluptatum nesciunt rem distinctio debitis sapiente molestias, culpa perspiciatis impedit rerum minima minus, labore provident beatae. Aliquam, tenetur nisi mollitia consequuntur ex, quis illo blanditiis maxime optio, possimus atque et.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt placeat nihil quo architecto nostrum mollitia optio! Voluptas, mollitia facilis hic voluptatum nesciunt rem distinctio debitis sapiente molestias, culpa perspiciatis impedit rerum minima minus, labore provident beatae. Aliquam, tenetur nisi mollitia consequuntur ex, quis illo blanditiis maxime optio, possimus atque et.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Rohit",
        "date": date(2022, 11, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Raj",
        "date": date(2023, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }

]

# Create your views here.


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-details.html", {
        "post": identified_post
    })
