import os
from typing import List
import pathlib
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import uuid


user_id=str(uuid.uuid4)
directory_path=(os.getcwd()+'/papers/'+user_id)
os.makedirs(directory_path,exist_ok="True")

def clear_question_bank(directory_path):
    try:

        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        return True
    except OSError:
         return False

from db_utilities import delete_all_record
delete_all_record()

if (not clear_question_bank(directory_path)):
    print("error in clearing the question bank")


