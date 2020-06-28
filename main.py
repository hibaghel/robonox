# the main script will will be run by RPi
import deliveryMotors
import rotating
import unloading

if __name__ == "__main__":
    
    unloading.forward()

    # scan package for pincode 
    pincode = rotating.get_pincode()

    # deliver to cart associated with the pincode 
    deliveryMotors.deliver(pincode)


