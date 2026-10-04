import requests

def find_product_by_barcode(barcode):
    url = f"https://world.openfoodfacts.org/api/v3.6/product/{barcode}.json"

    headers = {
        "User-Agent": "InventoryApp/1.0 (dorothy@school.com)" 
    }

    response = requests.get(url, headers=headers)

    if response.status_code!= 200:
        print(f"Status code: {response.status_code}")
        return None

    data = response.json()

    if data.get("status") == "success":
        return data.get("product")

    return None

if __name__ == "__main__":
    product = find_product_by_barcode("3274080005003")

    if product:
        print("Product:", product.get("product_name"))
        print("Brand:", product.get("brands"))
        print("Barcode:", product.get("code"))
        print("Quantity:", product.get("quantity"))
    else:
        print("Product not found")