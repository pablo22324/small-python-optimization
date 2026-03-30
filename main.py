import pandas as pd
import requests
import re
# importing csv file
df = pd.read_csv("keyword.csv", encoding="utf-16",header=0, sep="\\t")

base= "https://ahrefs.com/keyword-difficulty/?country=us&input="
l=0


browse=""
data=[]

# handling search results
def google_search():
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api,
        "cx": cx,
        "q": google,
        "num": 3
    }
    r = requests.get(url, params=params)
    if r.status_code != 200:
        print("error:", r.status_code, r.text)
        return []
    data = r.json()
    results = []
    for item in data.get("items", []):
        results.append({
            "title": item["title"],
            "link": item["link"],
        })
    return results
# support for the function that extracts keywords from the search engine
for i in df["Keyword"]:
    google=i
    l+=1
    if l==18:
        break


    if __name__ == "__main__":
        results = google_search()
        links = [item["link"] for item in results]
        links= " ".join(links)
        data.append(links)
        links=""
df["link"]=base + df["Keyword"]

for i, link_str in enumerate(data):
    df.at[i, 'results'] = link_str

# creating xlsx file with created data
df.to_excel("test.xlsx", index=False, header=["Keyword","Avg. monthly searches", "Link","results"])
# Zapis do Excela