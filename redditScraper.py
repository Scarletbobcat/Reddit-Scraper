import praw

reddit = praw.Reddit(client_id='hdcvNosfFtsG7qWKTvz9yg', client_secret='qCvJOwr709QWgqHA-pV_Zvb4EviPOg', user_agent='Testing')

sub1 = reddit.subreddit('EngineeringStudents')

sub2 = reddit.subreddit('drones')

filename = "drones&engineering.csv"

f = open(filename, "w")

headers = "Post Title, Post Url\n"

f.write(headers)

for submission in sub1.search("drones", sort="hot", limit=10):
    title = submission.title
    url = submission.url
    title = title.replace(',', '')
    f.write(title + ',' + url + '\n')

for submission in sub2.search("engineer", sort="hot", limit=10):
    title = submission.title
    url = submission.url
    title = title.replace(',', '')
    f.write(title + ',' + url + '\n')

f.close()