import re

text = "PythonTutorialAndExercises"

print(re.findall('[A-Z][^A-Z]*', text))