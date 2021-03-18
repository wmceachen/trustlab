import gzip
import re
from collections import Counter
#https://economictimes.indiatimes.com/definition/category/Economy
# URL_MATCH = '(?<=WARC-Target-URI: ).*'
# # URL_MATCH = 'WARC-Target-URI:'
ECON_WORDS = ['GDP',     
    'Asset Turnover Ratio',
    'Bailout',
    'Balance Of Payment',
    'Bank Rate',
    'Base Rate',
    'Broad Money To Reserve Money',
    'Call Money Rate',
    'Capacity Cost',
    'Capital Account',
    'Capital Adequacy Rati,o'
    'Capital Market',
    'Ceteris Paribus',
    'Clearing Price',
    'Consumer Price Index',
    'Consumer Surplus',
    'Contagion',
    'Contractionary Policy,'
    'Core Inflation',
    'Cost Benefit Analysis,'
    'Cost Push Inflation',
    'Countervailing Duties,'
    'Credit Default Swaps',
    'Cross Elasticity Of Demand',
    'Crowding Out Effect',
    'Currency Deposit Rati,o'
    'Deadweight Loss',
    'Debt Equity Ratio',
    'Deflation',
    'Depreciation',
    'Depression',
    'Dividend Signaling',
    'Domestic Institutiona,l Invest'
    'Due Date Rate',
    'Ease Of Doing Busines,s'
    'Etf',
    'Exchange Rate',
    'Fair Trade Price',
    'Fallout Risk',
    'Gross Domestic Saving,'
    'Gross National Produc,t'
    'Human Development Ind,ex'
    'Imperfect Competition,'
    'Indifference Curve',
    'Inferior Goods',
    'Infrastructure Invest,ment' 
    'Investment Banking',
    'Invisible Hand',
    'Labour Market',
    'Law Of Demand',
    'Law Of Supply',
    'Libor',
    'Liquid Asset',
    'Liquidity',
    'Liquidity Trap',
    'Macroeconomics',
    'Marginal Standing Facility',
    'Market Capitalization',
    'Mark To Market',
    'Mibor',
    'Microeconomics',
    'Monetary Policy',
    'Money Supply',
    'Monopoly',
    'Moral Hazard',
    'Mumbai Interbank Bid Rate', 
    'Net Interest Income (nii)',
    'Net National Income',
    'Non Performing Assets,'
    'Paradox',
    'Paradox Of Thrift',
    'Pareto\'s Efficiency',
    'Payments Banks',
    'Percentage Point',
    'Perfect Competition',
    'Phillips Curve',
    'Poverty Trap',
    'Price Ceiling',
    'Price Floor',
    'Price Mechanism',
    'Principle Agent Problem',
    'Privatization',
    'Producer Surplus',
    'Production Gap',
    'Production Possibility Fr',
    'Profitability Index',
    'Property Tax',
    'Proportional Tax',
    'Public Distribution System',
    'Purchasing Power Parity',
    'Quantitative Easing',
    'Quantity Demanded',
    'Quantity Supplied',
    'Quantity Theory Of Mo,ney'
    'Rational Behaviour',
    'Real Business Cycle Theory',
    'Real Economic Growth Rate',
    'Real Gdp At Factor Cost',
    'Recession',
    'Recessionary Gap',
    'Regressive Tax',
    'Regulatory Risk',
    'Rent Seeking',
    'Repo Rate',
    'Reserve Ratio',
    'Residual Claimant',
    'Revealed Preferences',
    'Reverse Repo Rate',
    'Satisficing',
    'Search Costs',
    'Seasonal Adjustment',
    'Secondary Market',
    'Securitization',
    'Service Tax',
    'Shareholder Value',
    'Social Capital',
    'Soft Currency',
    'Soft Loans',
    'Sovereign Risk',
    'Special Drawing Rights',
    'Speculation',
    'Speculative Motive',
    'Statutory Liquidity Ratio',
    'Stimulus Package',
    'Tender Period',
    'Trade Union',
    'True Cost Economics',
    'Tulip Mania',
    'Underwriting',
    'Unemployment Trap',
    'Union Budget',
    'Velocity Of Circulation',
    'Venture Capital',
    'Windfall Gains',
    ]
COVID_WORDS = ['covid', 'covid-19', 'pandemic']
NEWS_WORDS = ['news', 'journal', 'post', 'reporter']
def is_any(string:str, options:[str]):
    return any(o.lower() in string for o in options)

def has_some(string:str, options:[str], req=5):
    count = Counter(string.split())
    return sum(count[o.lower()] for o in options) > req
def text_thing(page_text):
    url, _, text = page_text.partition('\r')
    text = text.lower()
    if has_some(text, COVID_WORDS) and has_some(text, ECON_WORDS) and has_some(text, NEWS_WORDS):
        # print([o.lower() for o in ECON_WORDS if o.lower() in text])
        return True
    return False

with gzip.open('CC-MAIN-20201206002041-20201206032041-00719.warc.wet.gz', 'rb') as f:
    file_content = f.read().decode("utf-8")
    # print(file_content)
    # print(type(file_content))
    # m = re.findall(URL_MATCH, file_content)
    # print(m)
    print(len(list(filter(text_thing, file_content.split('WARC-Target-URI: ')))))
    
#iterate through, every time we find a URI reset bools about covid and economy, then look for next