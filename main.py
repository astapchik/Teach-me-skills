import os
from dotenv import load_dotenv

load_dotenv()

INTEGER_VAR = os.getenv('INTEGER_VAR')
print(INTEGER_VAR)
