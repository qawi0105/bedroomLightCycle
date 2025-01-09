import time

def smart_lighting_cycle():
    # Time duration for each stage (in seconds)
    lights_on_duration = 10   # Lights fully on
    dimming_duration = 5      # Lights dimmed
    lights_off_duration = 10  # Lights off

    while True:
        # Lights On
        print("Lights are ON: Full brightness")
        time.sleep(lights_on_duration)
        print("Lights are about to DIM")
        time.sleep(1)  # Short transition

        # Dimming Lights
        print("Lights are DIMMED: Low brightness")
        time.sleep(dimming_duration)
        print("Lights are about to TURN OFF")
        time.sleep(1)  # Short transition

        # Lights Off
        print("Lights are OFF")
        time.sleep(lights_off_duration)
        print("Cycle restarting...\n")
        time.sleep(1)  # Short break before restarting the cycle

# Run the smart lighting cycle
smart_lighting_cycle()
