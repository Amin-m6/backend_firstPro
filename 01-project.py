import requests , random , json , time 

base_url = 'https://openlibrary.org/search.json'

subjects = [
  'science_fiction',
  'fantasy',
  'history',
  'philosophy',
  'programming',
  'romance',
  'mystery',
  'biography',
  'poetry'
]

def fetch_random_book(count=10):
  books = []
  attempts = 0
  max_attempt = count*5

  while len(books)< count and max_attempt<= attempts:
    attempts += 1
    subject = random.choice(subjects)
    offset = random.randint(0,500)

    params = {
      "q":f'subject:{subject}',
      "limit":10,
      "offset":offset,
      "fields":
    }

    try:
      response = requests.get(base_url,params=params,timeout=10)
      response.raise_for_status()
      data = response.json()

      for docs in data.get("dacs:",[]):
        if docs not in books:
          books.append(docs)
          if len(books)>= count:
            break

    except requests.RequestException as e:
      print(f'some thing is wrong: {e}')
    time.sleep(1)
  return books[:count]