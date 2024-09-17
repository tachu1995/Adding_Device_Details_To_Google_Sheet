import datetime
from zoneinfo import ZoneInfo
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define the scope
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a  spreadsheet.
SPREADSHEET_ID = "18Nw59T0uchyj-zQp-K_EXkL0FVXLFQuFJWjtJuwa83A"
# Range Would Not Be important 
RANGE_NAME = "Sheet1!A1:E" 
#Define the token
creds = Credentials.from_service_account_file("token.json", scopes=SCOPES)

#Define the time
local = ZoneInfo("Australia/Melbourne")
date = datetime.datetime.now(local).strftime("%Y-%m-%d %H:%M")



def lambda_handler(event, context):
    
    PO_number = event["PO_number"] 
    imei = event["imei"]
    SKU = event["SKU"]
    product_name = event["model"] 
    device_color = event["color"] 
    device_grade = event["combine_grade"]
    make = event["make"]
    capacity = event["cap"]
    device_location = event["device_location"]
    tech = event['tech']
    serial = event["serial"]
    
    
    data = [[date,imei,serial,SKU,make,product_name,capacity,device_color,PO_number,device_grade,device_location,tech]]
    
    try:
        service = build("sheets", "v4", credentials=creds)
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, insertDataOption="INSERT_ROWS", valueInputOption="USER_ENTERED",
                                  body={"values":data})
            .execute()
        )
        # TODO implement
        return {
            'statusCode': 200
        }
        
    except HttpError as err:
        return {
            'statusCode': 201
        }
