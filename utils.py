import gzip
BUCKET_BASE_PATH = 's3://commoncrawl/'
def get_paths():   
    paths = []
    with gzip.open(f'wet.paths.gz') as f:
        paths.extend(map(lambda p: BUCKET_BASE_PATH + p, f.read().decode("utf-8").splitlines()))
    return paths

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