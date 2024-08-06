import re

# Utility functions, for example:
def clean_description(description):
    description = re.sub(r'<br\s*?/?>', '', description)
    description = re.sub(r'<i\s*?>|</i>', '', description)
    return description

# Add other utility functions here
