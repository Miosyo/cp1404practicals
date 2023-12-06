import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

prompt = input("Search: ")
try:
    page = wikipedia.page(prompt)
    print(page.title)
    print(page.summary)
    print(page.url)
except DisambiguationError:
    print('Disambiguation Error')
except PageError:
    print('Page not found')
