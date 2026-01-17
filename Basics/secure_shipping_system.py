import time

# --- 1. GLOBAL SCOPE ---
total_shipped_items = 0

# --- 2. THE AUTHORIZER (Decorator with 3-Attempt Logic) ---
def admin_only(fun):
    def wrapper(*args, **kwargs):
        # Using range(3) to give exactly 3 chances
        for attempt in range(3):
            password = input(f"Attempt {attempt + 1}/3 - Enter Admin Password: ")
            
            if password == "ship99":
                print(" Access Granted! Initializing Shipping System...")
                return fun(*args, **kwargs)
            else:
                print(f" Incorrect. {2 - attempt} attempts left.")
        
        # Runs only if the loop finishes without a 'return'
        print(" Security Lock: Access Denied. Contact System Admin.")
        return None
    return wrapper

# --- 3. THE ID FACTORY (Generator for Memory Efficiency) ---
def generate_ids(count):
    start_id = 1001
    for i in range(count):
        # Yields one ID at a time in the specified format
        yield f"TRK-{start_id + i}"

# --- 4. THE SHIPPING LOGIC (Function + Lambda) ---
@admin_only
def process_shipping(items_dict, zone="North"):
    global total_shipped_items
    
    # Lambda for 5% International Tax calculation
    tax_calc = lambda price: price * 0.05
    
    # Initialize the ID generator based on the number of items
    id_generator = generate_ids(len(items_dict))
    
    print(f"\n{'='*40}")
    print(f" SHIPPING MANIFEST | ZONE: {zone}")
    print(f"{'='*40}")
    
    for name, price in items_dict.items():
        # Calculate Tax and Total
        tax = tax_calc(price)
        final_price = price + tax
        
        # Pull the next ID from the generator
        tracking_id = next(id_generator)
        
        print(f"ID: {tracking_id} | Item: {name:10} | Total: ${final_price:>8.2f}")
        
        # Update global warehouse counter
        total_shipped_items += 1
    
    print(f"{'='*40}")
    print(f"Session Complete. {len(items_dict)} items processed.")

# --- 5. EXECUTION ---
if __name__ == "__main__":
    # Test Data: A dictionary of items and their base prices
    warehouse_orders = {
        "Laptop": 1200.00,
        "Monitor": 350.00,
        "Keyboard": 45.00,
        "Webcam": 85.00
    }

    # Calling the decorated function
    process_shipping(warehouse_orders, zone="International")

    print(f"\n Global Warehouse Total: {total_shipped_items} items shipped.")
