from blog import Blog

blogs = dict()  # blog_name : blog_object
MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one,"p" to create a post, or "q" to quit'
POST_TEMPLATE = '''
---{}---

{}

'''


def menu():
    # show the user the available blog
    # let the user make a choice from shown menu
    # make an action with that choice
    # eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


def ask_create_blog():
    title = input('what would you like to title this blog post? ')
    author = input('what is your name? ')

    blogs[title] = Blog(title, author)


def ask_read_blog():
    title = input('what is the blog you would like to read? ')

    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_name = input('what is the name of the title you would like to write? ')
    title = input('what is the title of your article ? ')
    content = input('please write your content here. ')

    blogs[blog_name].create_post(title, content)

