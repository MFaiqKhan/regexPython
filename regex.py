import re 

# Regex pattern to match a valid phone number 

text= "My phone number is (123)-456-7890 and my friend's number is 0123456789"

pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'

matches = re.findall(pattern,text) # returns a list of all the matches in the text
print(matches) # output: ['(123)-456-7890', '0123456789']

# Regex Pattern to extract note title from the tesla_report_notes.jpg file name 


text2 = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''

pattern = 'Note \d - ([^\n]*)' # [^\n]* means any character except new line so it will match the title of the note and 
# brackets are used to group the pattern means we want to extract the title of the note and not the whole line with the note number

matches = re.findall(pattern,text2)
print(matches) # output: ['Overview', 'Summary of Significant Accounting Policies']


# 3.)

text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
FY2023 Q5 is a not a valid quarter.
'''

# get the year from the text
pattern = 'FY\d{4} Q[1-4]' # FY\d{4} means FY followed by 4 digits and Q[1-4] means Q followed by 1,2,3 or 4, 1-4  means 1 to 4 is a range
matches = re.findall(pattern,text)
print(matches) # output: ['FY2021 Q1', 'FY2020 Q4']

# 4.) without FY

pattern = 'FY(\d{4} Q[1-4])' # () is used to group the pattern and we want to extract the year and quarter from the text
matches = re.findall(pattern,text)
print(matches) # output: [('2021 Q1',), ('2020 Q4',)]


# 5.) Case insensitive pattern match using flags

text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''

pattern = 'FY\d{4} Q[1-4]'
matches = re.findall(pattern, text, flags=re.IGNORECASE)
print(matches) # output: ['FY2021 Q1', 'fy2020 Q4']


# 6.) Extract only financial numbers

text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. 
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''

pattern = '\$\d[0-9\.]+' # \d means any digit and [0-9\.]+ means any digit or a dot
matches = re.findall(pattern, text) 
print(matches) # output: ['$4.85', '$3']

# 7.) Extract periods and financial numbers both


pattern = 'FY(\d{4} Q[1-4])[^\$]+\$([0-9\.]+)' 
matches = re.findall(pattern, text)
print(matches) # output: [('2021 Q1', '4.85'), ('2020 Q4', '3')] 

# 8.) re.search


# output: ('2021 Q1', '4.85') this is the first match of the pattern and the groups are extracted

text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 ljh lsj a 123 was $4.85 billion. Same number for FY2020 Q4 was $8 billion
'''
pattern = 'FY(\d{4} Q[1-4])[^\$]+\$([0-9\.]+)'
match = re.search(pattern, text) # returns the first match
print(match) # output: <re.Match object; span=(67, 84), match='FY2021 Q1 ljh lsj a 123'> this is the first match of the pattern
print(match.groups()) # output: ('2021 Q1', '4.85') this is the first match of the pattern and the groups are extracted