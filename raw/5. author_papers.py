import pandas as pd
import json

VENUE = "oral"
VENUE = "spotlight"
VENUE = "poster"

paper_authors = {}
author_papers = {}
papers = json.load(open(f"data/neurips2025_{VENUE}.json"))
for paper in papers:
    paper_title = paper['content']['title']['value']
    authors = paper['content']['authorids']['value']
    paper_authors[paper_title] = authors
    for author in authors:
        if author not in author_papers:
            author_papers[author] = []
        author_papers[author].append(paper_title)

print(f"VENUE: {VENUE}")
print(f"There are {len(paper_authors)} papers")
print(f"There are {len(author_papers)} authors")

author_npapers = {}
for author, papers in author_papers.items():
    author_npapers[author] = len(papers)

json.dump(author_papers, open(f"data/neurips2025_{VENUE}_author_papers.json", "w"), indent=2)

df = pd.DataFrame(author_npapers.items(), columns=['author', 'n_papers'])
df.sort_values(by='n_papers', ascending=False, inplace=True)
print(df.head(10))
