import pandas as pd
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def is_valid_email(email):
    url = "https://email-validator28.p.rapidapi.com/email-validator/validate"
    querystring = {"email":email}
    headers = {
        "X-RapidAPI-Key": "your_x_rapid_api_key ",
        "X-RapidAPI-Host": "mailcheck.p.rapidapi.com"
    }
    logging.info(f"Checking validity of email: {email}")
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        if "valid" in data:
            return data["valid"]
        else:
            logging.error(f"Error: 'valid' key not found in response for email: {email}")
            logging.error(f"Response: {data}")
            return False
    else:
        logging.error(f"Error: {response.status_code}")
        logging.error(f"Response: {response.text}")
        return False

# Read input CSV file
input_df = pd.read_csv("input.csv")

# Filter valid emails
valid_emails = []
for email in input_df["email"]:
    if is_valid_email(email):
        valid_emails.append(email)

# Create DataFrame for output CSV
output_df = pd.DataFrame({"email": valid_emails})

# Write output CSV file
output_df.to_csv("output.csv", index=False)
