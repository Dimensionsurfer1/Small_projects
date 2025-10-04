from google import genai

client = genai.Client()
def generate_blog_post(paragraph_topic):
    response = client.models.generate_content(
        model = "gemini-2.5-flash", 
        contents=  "Write a detailed blog post about the following topic in about 100 words : " + paragraph_topic,
    )
    retrieve_blog = response.text
    return retrieve_blog
use_ai = int(input('do you want to use AI to generate a blog post? for yes type 1, for no type 0: '))
if use_ai == 1:
    topic = input('type the topic of your blog post here: ')
    blog_post = generate_blog_post(topic)
    print('----please wait while your blog post is being generated----')
    print('Here is your generated blog post:')
    print(blog_post)
elif use_ai == 0:
    print('ok, maybe next time!')
    exit()
else:
    print('input not recognized, please type 1 or 0')
    exit()