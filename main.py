import json
import pandas as pd

df = pd.read_csv("neurips25_author_profiles.csv")

print(df.info())
print("Shape: ", df.shape)
print("Columns: ", df.columns)

df.fillna("", inplace=True)


for index, row in df.iterrows():
    author_id, preferredEmail, gender, gscholar, emails, names, history, relations, emailsConfirmed, homepage, pronouns, expertise, dblp, orcid, linkedin, semanticScholar, aclanthology, wikipedia = row
    
    if emails != "":
        emails = json.loads(emails)
    if names != "":
        names = json.loads(names)
    if history != "":
        history = json.loads(history)
    if relations != "":
        relations = json.loads(relations)
    if emailsConfirmed != "":
        emailsConfirmed = json.loads(emailsConfirmed)
    
    if expertise != "":
        expertise = json.loads(expertise)

    print(f"Author ID: {author_id}")
    print(f"Preferred Email: {preferredEmail}")
    print(f"Gender: {gender}")
    print(f"GScholar: {gscholar}")
    print(f"Emails: {emails}")
    print(f"Names: {names}")
    print(f"History: {history}")
    print(f"Relations: {relations}")
    print(f"Emails Confirmed({len(emailsConfirmed)}): {emailsConfirmed}")
    print(f"Homepage: {homepage}")
    print(f"Pronouns: {pronouns}")
    print(f"Expertise: {expertise}")
    print(f"DBLP: {dblp}")
    print(f"ORCID: {orcid}")
    print(f"LinkedIn: {linkedin}")
    print(f"Semantic Scholar: {semanticScholar}")
    print(f"ACL Anthology: {aclanthology}")
    print(f"Wikipedia: {wikipedia}")
    print("================================================")
    break
