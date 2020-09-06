import sqlite3
import matplotlib.pyplot as plt
import tldextract
import numpy as np
from collections import defaultdict
from collections import Counter

websiteToNum_v = [0] * 100
thirdPartyToNum_v = defaultdict(int)
websiteToNum_a = [0] * 100
thirdPartyToNum_a = defaultdict(int)

def count_url(con, websiteToNum, thirdPartyToNum):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT script_url, visit_id FROM javascript')
    
    rows = cursorObj.fetchall()
    for row in rows:
        thirdParty = tldextract.extract(row[0]).registered_domain
        websiteToNum[row[1]-1] += 1
        thirdPartyToNum[thirdParty] += 1
    
    cursorObj.close()
    con.close()

def plot_thirdParty_distribution(y_ublock, y_vanilla):
    plt.title("Distribution of JavaScript API Calls")
    plt.xlabel("Top 100 Websites")
    plt.ylabel("Number of JavaScript API Calls")
    plt.plot(y_vanilla, label="Vanilla Mode")
    plt.plot(y_ublock, label="Ad-Block Mode")
    plt.legend()
#    plt.show()
    plt.savefig('js.png')
    

def list_ten_top_website(y_ublock, y_vanilla):
    v_top_10 = Counter(y_vanilla).most_common(10)
    a_top_10 = Counter(y_ublock).most_common(10)
    print("Top-10 Most Popular Third-party Domains in Vanilla Mode")
    for url in v_top_10:
        print(url)
        
    print("Top-10 Most Popular Third-party Domains in Ad-Block mode")
    for url in a_top_10:
        print(url)
    

ad_con = sqlite3.connect("./data/adblock.sqlite")
count_url(ad_con, websiteToNum_a, thirdPartyToNum_a)


va_con = sqlite3.connect("./data/vanilla.sqlite")
count_url(va_con, websiteToNum_v, thirdPartyToNum_v)

list_ten_top_website(thirdPartyToNum_a, thirdPartyToNum_v)
plot_thirdParty_distribution(websiteToNum_a, websiteToNum_v)

