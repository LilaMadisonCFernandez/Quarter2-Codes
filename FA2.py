#Defining the Function
def calculate_delivery_fee(distance, rate):
    total_fee = distance * rate
    return total_fee

#Main Program
distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

fee = calculate_delivery_fee(distance, rate)

print(f"Total Delivery Fee: ₱{fee:.2f}")
