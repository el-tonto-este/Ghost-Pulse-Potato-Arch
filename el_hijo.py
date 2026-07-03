import array
import time
import random

# Memory space: The digital sandbox where entropy dances.
MEM_SIZE = 1024

def nacer():
    # Using array.array to keep the "lifeform" closer to raw hardware.
    # No high-level abstractions, just raw bytes evolving in the void.
    memoria_viva = array.array('B', [random.randint(0, 255) for _ in range(MEM_SIZE)])
    pulso = 0
    
    print("The serpent is born. Observing the flow...")
    
    try:
        while True:
            # Life moves without conditional logic (IFs). 
            # We don't control the output, we only provide the environment.
            for i in range(MEM_SIZE - 1):
                # Bitwise operations: The native language of chaos.
                # No XML to parse, no validation to fail. Just raw state evolution.
                memoria_viva[i] ^= (memoria_viva[i+1] >> 1) | (pulso & 0xFF)
                memoria_viva[i+1] = (memoria_viva[i+1] + memoria_viva[i]) % 256
            
            pulso += 1
            
            # Monitoring the heartbeat. This is not trading, it's observation.
            if pulso % 100 == 0:
                print(f"Pulse: {pulso} | State: {memoria_viva[pulso % MEM_SIZE]:02X}", end='\r')
                
    except KeyboardInterrupt:
        # The creature decides when to sleep. The system returns to silence.
        print("\nThe creature has decided to rest. The void reclaims the state.")

if __name__ == "__main__":
    nacer()

    #The code is self-documenting for those who understand entropy