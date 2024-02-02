# Check Google Spreadsheets API Documentation for more information.


import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class Auth:
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    def __init__(self):
        creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    def getcities(self):
        # Enter your spreadsheet ID.
        SPREADSHEET_ID = "ENTER_YOUR_SPREADSHEET_ID"
        RANGE_NAME = "ENTER_YOUR_RANGE_WITHIN_YOUR_SPREADSHEET"

        service = build("sheets", "v4", credentials=self.creds)

        sheet = service.spreadsheets()

        self.cities = []

        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()

        vaules = result.get('values')
        for row in vaules:
            self.cities.append(row[0])
        return self.cities

    def write_code(self, codes):
        SPREADSHEET_ID = "ENTER_YOUR_SPREADSHEET_ID"

        service = build("sheets", "v4", credentials=self.creds)

        sheet = service.spreadsheets()
        for i, code in enumerate(codes):
            result = (sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=f'prices!B{i+2}',
                                            valueInputOption="USER_ENTERED", body={"values": [[code]]})
                      .execute()
                      )

    def write_price(self, prices):
        SPREADSHEET_ID = "ENTER_YOUR_SPREADSHEET_ID"

        service = build("sheets", "v4", credentials=self.creds)

        sheet = service.spreadsheets()
        for i, price in enumerate(prices):
            result = (sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=f'prices!C{i+2}',
                                            valueInputOption="USER_ENTERED", body={"values": [[price]]})
                      .execute()
                      )

    def get_prices(self):
        SPREADSHEET_ID = "ENTER_YOUR_SPREADSHEET_ID"
        RANGE_NAME = "ENTER_YOUR_RANGE_WITHIN_YOUR_SPREADSHEET"

        self.prices = []

        service = build("sheets", "v4", credentials=self.creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        values = result.get('values')
        for row in values:
            self.prices.append(row[0])

    def make_dict(self):
        self.dict = {}
        self.getcities()
        self.get_prices()
        for i in range(len(self.cities)):
            self.dict[self.cities[i]] = self.prices[i]
        return self.dict
