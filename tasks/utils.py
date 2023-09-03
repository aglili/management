from trycourier import Courier
import os 
from dotenv import load_dotenv
load_dotenv()




def send_task_email(username:str,email:str,due_date,description:str,assigner:str):
    client = Courier(auth_token=os.getenv("COURIER_KEY"))
    client.send_message(
    message={
        "to": {
        "email": email,
        },
        "template": "FB6KP7XAXHM8ZQPE1EZHP47YWG50",
        "data": {
        "Name": username,
        "date": due_date,
        "AssignmentDetails": description,
        "YourName": assigner,
        },
    }
    )
    

