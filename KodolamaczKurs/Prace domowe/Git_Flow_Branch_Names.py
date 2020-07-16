import re

DATA = [
    'master',
    'develop',
    'release/1.0',
    'feature/ID-1337-some-new-feature',
    'bugfix/ID-1337-fixing-old-bug',
    'hotfix/ID-1337-bug-on-production',
    "pull-request/42"
]

PATTERN = r'^(feature|bugfix|hotfix)\/([A-Z]{2,10})-([1-9])([0-9]{0,4})-([a-z0-9-]{0,30})|(master)|(develop)|(release/[1-9]\.[0-9])|(pull-request\/[1-9]*[0-9])$'
result = [[True, data] if re.match(PATTERN, data) else [False, data] for data in DATA]
print(*result, sep='\n')