# This is a story of a brave explorer who is seeking to find new life on an unknown Galaxy
# A space-based adventure of a crew of curious individuals exploring an unknown galaxy.
import random
import time
print("Andromeda explorers. version 0.0.1")
username = input("Please insert your name: ")

def intro():
 print(f"Welcome aboard {username}, you and your crew are flying straightaway to Andromeda galaxy")
 time.sleep(2.5)
 print("During this Journey, your ship, Aegis IV, has suffered an irreversible damage after a hyperspace jump")
 time.sleep(4)
 print("quantum core is unstable..., and there is enough fuel and capacity for one last jump")
 time.sleep(4)
 print("good news are that we have three potential options near your ship: ")
 time.sleep(3)
 print("(1). Eltharion-3 / Ocean world, possible microbial life. You'd sacrifice, but you'd be the first one on finding life outside Earth.")
 time.sleep(2)
 print("(2). Nhalora Prime / Desert world, rare energy resources. A chance to refuel and keep exploring.")
 time.sleep(2)
 print("(3). Vaelion Theta / Dark region, faint signals... unknown.")

def eltharion_3():
    print("Jumping to Eltarion_3...")
    time.sleep(5)
    print("Upon arrival, you sense a breathable atmosphere and calm oceans.")
    time.sleep(3)
    event = random.choice(["lifeform", "storm", "ancient_ruins"])
    if event == "lifeform":
        print("you discover bioluminescent organisms in the shallow waters. They react to your presence...")
        decision = input("Do you collect a sample (1) or observe from the ship (2)? ")
        if decision == "1":
            print("The sample contaminates the air filters! Crew health deteriorates...")
        else:
            print("You safely observe and take valuable notes about it. Science wins the day!...")
    elif event == "storm":
        print("A magnetic storm strikes the ship! You must decide whether to lift off or hold position...")
        position = input(f" What shall we do {username} ? Shall we lift off (1) or hold position (2)? : ")
        if position == "1":
            print("The pods launch safely, but the Aegis IV is lost forever... right?")
        else:
            print("You hold your ground, ship barely survives but crew is traumatized.")
    else:
        print("You have found alien ruins. Something... is watching from the shadows.")
        decision = input("Do you send a landing team (1) or scan from orbit (2)? ")
        if decision == "1":
            print("The landing team disappears without a trace...")
        else:
            print("Scans reveal a massive structure, possibly a dormant AI core.")
    time.sleep(3)
    print("Your crew records this day as a new beginning-or the start of the end.")

def nhalora_prime():
    print("Jumping to Nhalora Prime...")
    time.sleep(4)
    print("A vast desert stretches beneath twin suns.")
    time.sleep(3)
    event = random.choice(["artifact", "sandstorm", "mutation"])
    if event == "artifact":
        print("You uncover an ancient artifact emitting unknown energy signatures...")
        decision = input("Do you try to activate the artifact (1) or store it for later study (2)? ")
        if decision == "1":
            print("The artifact emits a burst of radiation, damaging ship systems")
        else:
            print("You secure it in a containment field. Future scientists will thank you...")
    elif event == "sandstorm":
        print("A metallic sandstorm batters the hull! Oxygen systems are falling...")
    else:
        print("A crew member begins mutating due to high radiation levels...")
        time.sleep(3)
        print("Nhalora Prime fades behind you, but something aboard has changed forever.")

def vaelion_theta():
        print("Jumping to Vaelion Theta...")
        time.sleep(4)
        print("Total darkness surrounds the ship. Radar picks up echoes among the methane seas")
        time.sleep(3)
        event = random.choice(["hostile_contact", "scientific_discovery", "crew_isolation"])
        if event == "hostile_contact":
            print("An unknown lifeform boards the ship. There's no time to react!")
            decision = input("Do you seal the affected deck (1) or attempt communication (2)? ")
            if decision == "1":
                print("The deck is sealed, saving the ship, but you sacrificed part of the crew.")
            else:
                print("The creature replies; not with words, but with a telepathic image of your homeworld")
        elif event == "scientific_discovery":
            print("You detect impossible organic compounds on the surface- this could redefine current understanding of life.")
            decision = input("Do you send a probe (1) or descend manually (2)? ")
            if decision == "1":
                print("The probe transmits valuable data before melting under pressure.")
            else:
                print("The landing craft malfunctions, leaving you trapped on the surface...")
        else:
            print("All communications go dark. The crew begins to lose their minds...")
        time.sleep(3)
        print("Your ship drifts silently through the void, destined to become a cosmic legend.")

def main():
    intro()
    time.sleep(2.5)
    try:
        choice = int(input("Which system will you jump to? 1, 2 or 3?: "))
    except ValueError:
        print("Invalid input — you entered something that isn't a number.")
        return
    if choice == 1:
        eltharion_3()
    elif choice == 2:
        nhalora_prime()
    elif choice == 3:
        vaelion_theta()
    else:
        print("Invalid choice. Indecision seals your crews fate... :(")

if __name__ == "__main__":
    main()