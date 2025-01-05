# Electricity Billing System CLI Application
class ElectricityBillingSystem:
    def __init__(self, customer_name, units_consumed):
        self.customer_name = customer_name
        self.units_consumed = units_consumed
        self.unit_rate = self.get_unit_rate()
        self.total_amount = 0

    # Define the unit rate based on consumption
    def get_unit_rate(self):
        if self.units_consumed <= 100:
            return 5  # rate per unit for <= 100 units
        elif 101 <= self.units_consumed <= 300:
            return 7  # rate per unit for 101 to 300 units
        else:
            return 10  # rate per unit for > 300 units

    # Calculate the total bill amount
    def calculate_bill(self):
        self.total_amount = self.units_consumed * self.unit_rate
        return self.total_amount

    # Display the bill summary
    def generate_bill(self):
        print("\n------ Electricity Bill ------")
        print(f"Customer Name: {self.customer_name}")
        print(f"Units Consumed: {self.units_consumed} units")
        print(f"Rate per Unit: {self.unit_rate} Rs")
        print(f"Total Amount: {self.calculate_bill()} Rs")
        print("-----------------------------\n")


# Main function to run the CLI application
def main():
    print("Welcome to the Electricity Billing System!")
    
    # Get user input for customer name and units consumed
    customer_name = input("Enter Customer Name: ")
    units_consumed = int(input("Enter Units Consumed: "))
    
    # Create an instance of the ElectricityBillingSystem
    billing_system = ElectricityBillingSystem(customer_name, units_consumed)
    
    # Generate and display the bill
    billing_system.generate_bill()

if __name__ == "__main__":
    main()
