from django.shortcuts import render


# dummy data
post = [
    {
        'author': 'Christian',
        'title': 'Blog Post #1',
        'content': 'First post content.',
        'date_posted': 'October 28, 2019'
    },
    {
        'author': 'Bethany',
        'title': 'Blog Post #2',
        'content': 'Second post content.',
        'date_posted': 'October 22, 2019'
    }
]


def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
