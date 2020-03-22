headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

space_count = 0
news_ticker = ""

for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)
print(len(news_ticker))

"""
output
Local Bear Eaten by Man Legislature Announces New Laws Peasant Discovers Violence Inherent in System Cat Rescues Fireman Stuck in Tree Brave
140
"""
