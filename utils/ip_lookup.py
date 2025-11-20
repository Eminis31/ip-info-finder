# import requests

# def lookup_ip(ip_address):
#     url = f"https://ipapi.co/{ip_address}/json/"
    
#     try:
#         response = requests.get(url, timeout=5)
#         data = response.json()

#         if "error" in data:
#             return {"error": "Invalid IP address or lookup failed"}

#         return {
#             "ip": data.get("ip"),
#             "city": data.get("city"),
#             "region": data.get("region"),
#             "country": data.get("country_name"),
#             "latitude": data.get("latitude"),
#             "longitude": data.get("longitude"),
#             "timezone": data.get("timezone"),
#             "org": data.get("org"),
#         }

#     except Exception as e:
#         return {"error": str(e)}





import requests
import ipaddress

def lookup_ip(ip_address):
    ip_address = (ip_address or "").strip()
    if not ip_address:
        return {"error": "IP address is empty"}

    try:
        # validate IP format
        ipaddress.ip_address(ip_address)
    except ValueError:
        return {"error": "Invalid IP address format"}

    url = f"https://ipapi.co/{ip_address}/json/"

    try:
        response = requests.get(url, timeout=5)
        if not response.ok:
            return {"error": f"HTTP error {response.status_code}"}

        try:
            data = response.json()
        except ValueError:
            return {"error": "Invalid JSON response from API"}

        if data.get("error"):
            # prefer API-provided message if available
            message = data.get("reason") or data.get("message") or "Invalid IP address or lookup failed"
            return {"error": message}

        return {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country_name"),
            "latitude": data.get("latitude") or data.get("lat"),
            "longitude": data.get("longitude") or data.get("lon"),
            "timezone": data.get("timezone"),
            "org": data.get("org"),
        }

    except requests.RequestException as e:
        return {"error": str(e)}
