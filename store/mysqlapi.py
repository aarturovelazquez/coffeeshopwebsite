import requests

# set the API endpoint URL
url = "http://127.0.0.1:8080/"

# set the request headers
headers = {
    "X-Api-Key": "YdyfzrxD0GRgIiDFHzGU3JjxrCmLIrf2hOOKSXsOO99jFplKX9DCaeSW5oGkjdF1",
    "Content-Type": "application/json"
}


def post_to_api(url, headers, newfirstname, newlastname, newemail, newaddress, newcountry, newcity, newzip, newproduct):

    # set the request payload
    payload = {
        "order_firstname": newfirstname,
        "order_lastname": newlastname,
        "order_email": newemail,
        "order_address": newaddress,
        "order_country": newcountry,
        "order_city": newcity,
        "order_zip": newzip,
        "order_products": newproduct,
    }

    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()
    return response_data


# new_insert = post_to_api(url, headers, "Irlanda", "Soto", "Irlanda@gmail.com", "Avenida Guadalupe 85", "Mexico", "Guadalajara", "44500", "H")
