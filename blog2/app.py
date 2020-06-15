MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one,"p" to create a post, or "q" to quit'

blogs = dict()  # blog_name : blog_object


def menu():
    # show the user the available blog
    # let the user make a choice from shown menu
    # make an action with that choice
    # eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))
