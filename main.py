# the main script will will be run by RPi
import deliveryMotors
import rotating

if __name__ == "__main__":
    
    # scan package for pincode 
    pincode = rotating.get_pincode()

    # deliver to cart associated with the pincode 
    deliveryMotors.deliver(pincode)
