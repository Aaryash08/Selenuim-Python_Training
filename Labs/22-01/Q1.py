import requests
import json

def fetch_users():
    url = "http://127.0.0.1:5000/users"

    # 2️⃣ Custom headers
    headers = {
        "User-Agent": "Python-Requests-Client",
        "Accept": "application/json"
    }
    try:
        # 1️⃣ Send GET request
        response = requests.get(url, headers=headers, timeout=5)

        # 5️⃣ Handle HTTP errors
        response.raise_for_status()

        # 3️⃣ Parse JSON response
        users = response.json()

        extracted_data = []

        for user in users:
            extracted_data.append({
                "id": user["id"],
                "name": user["name"],
                "email": user["email"]
            })

        # 4️⃣ Save extracted data to JSON file
        with open("users_data.json", "w") as file:
            json.dump(extracted_data, file, indent=4)

        print("User data successfully saved to users_data.json")

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API")

    except requests.exceptions.Timeout:
        print("Error: Request timed out")
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)


if __name__ == "__main__":
    fetch_users()
