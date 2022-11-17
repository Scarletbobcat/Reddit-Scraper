import praw

reddit = praw.Reddit(client_id='hdcvNosfFtsG7qWKTvz9yg', client_secret='qCvJOwr709QWgqHA-pV_Zvb4EviPOg', user_agent='Testing')

sub1 = reddit.subreddit('EngineeringStudents')
sub2 = reddit.subreddit('drones')

filename = "drones&engineering.csv"

f = open(filename, "w")

headers = "Post Title, Post Url, Post Desc, Post Comments ->\n"

f.write(headers)

for submission in sub1.search("drone", sort="top", time_filter="year", limit=5):
    title = submission.title.replace(',', '')
    url = submission.url
    f.write(title + ',' + url + ',' + submission.selftext.replace('\n', ' ').replace(',', '') + ',')
    for top_comment in submission.comments:
        body = top_comment.body.replace(',', '').replace('\n', ' ')
        f.write(body + ',')
    f.write('\n')

for submission in sub2.search("engineer", sort="top", time_filter="year", limit=5):
    title = submission.title.replace(',', '').replace('\n', ' ')
    url = submission.url
    f.write(title + ',' + url + ',' + submission.selftext.replace('\n', ' ').replace(',', '') + ',')
    for top_comment in submission.comments:
        body = top_comment.body.replace(',', '').replace('\n', ' ')
        f.write(body + ',')
    f.write('\n')

f.close()

# add top comments