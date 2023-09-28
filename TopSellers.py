import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Seller': [
        'Passe-Partout', 'Aziempire', 'Sniffraud', 'Usaccs',
        'The-Naughty-Nurse-Reserve', 'skizoom', 'hellbin',
        'KantFr', 'blackmanba1fe', 'LePetitPrince',
        'PapaGanja', 'Copek', 'Chapo'
    ],
    'Products': [
        8, 71, 92, 12, 17, 13, 90, 27, 12, 47, 32, 30, 18
    ],
    'Rating': [
        5, 3, 3, 3, 5, 4, 4, 4, 4, 4, 4, 4, 4
    ],
    'Feedback': [
        28, 19, 30, 33, 6, 187, 177, 93, 34, 435, 584, 202, 132
    ],
    'Transactions': [
        28, 19, 30, 33, 6, 187, 177, 93, 34, 435, 584, 202, 132
    ]
}

df = pd.DataFrame(data)

top_10_sellers = df.sort_values(by='Transactions', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_10_sellers['Seller'], top_10_sellers['Transactions'])
plt.xlabel('Seller')
plt.ylabel('Number of Transactions')
plt.title('Top 10 Sellers by Number of Transactions')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


