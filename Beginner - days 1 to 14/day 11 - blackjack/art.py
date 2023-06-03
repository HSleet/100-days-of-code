# ascii art blackjack logo
logo = """

▀█████████▄   ▄█          ▄████████  ▄████████    ▄█   ▄█▄      ▄█    ▄████████  ▄████████    ▄█   ▄█▄ 
  ███    ███ ███         ███    ███ ███    ███   ███ ▄███▀     ███   ███    ███ ███    ███   ███ ▄███▀ 
  ███    ███ ███         ███    ███ ███    █▀    ███▐██▀       ███   ███    ███ ███    █▀    ███▐██▀   
 ▄███▄▄▄██▀  ███         ███    ███ ███         ▄█████▀        ███   ███    ███ ███         ▄█████▀    
▀▀███▀▀▀██▄  ███       ▀███████████ ███        ▀▀█████▄        ███ ▀███████████ ███        ▀▀█████▄    
  ███    ██▄ ███         ███    ███ ███    █▄    ███▐██▄       ███   ███    ███ ███    █▄    ███▐██▄   
  ███    ███ ███▌    ▄   ███    ███ ███    ███   ███ ▀███▄     ███   ███    ███ ███    ███   ███ ▀███▄ 
▄█████████▀  █████▄▄██   ███    █▀  ████████▀    ███   ▀█▀ █▄ ▄███   ███    █▀  ████████▀    ███   ▀█▀ 
             ▀                                   ▀         ▀▀▀▀▀▀                            ▀         
"""
cards = {
    2: f"""
┌───────────────┐
│2              │
│# ┌─────────┐  │
│  │         │  │
│  │    #    │  │
│  │         │  │
│  │         │  │
│  │         │  │
│  │    #    │  │
│  │         │  │
│  └─────────┘ #│
│              2│
└───────────────┘
""",
    3: f"""
┌───────────────┐
│3              │
│# ┌─────────┐  │
│  │         │  │
│  │    #    │  │
│  │         │  │
│  │    #    │  │
│  │         │  │
│  │    #    │  │
│  │         │  │
│  └─────────┘ #│
│              3│
└───────────────┘
""",
    4: f"""
┌───────────────┐
│4              │
│# ┌─────────┐  │
│  │#       #│  │
│  │         │  │
│  │         │  │
│  │         │  │
│  │         │  │
│  │         │  │
│  │#       #│  │
│  └─────────┘ #│
│              4│
└───────────────┘
""",
    5: f"""
┌───────────────┐
│5              │
│# ┌─────────┐  │
│  │#       #│  │
│  │         │  │
│  │         │  │
│  │    #    │  │
│  │         │  │
│  │         │  │
│  │#       #│  │
│  └─────────┘ #│
│              5│
└───────────────┘
""",
    6: f"""
┌───────────────┐
│6              │
│# ┌─────────┐  │
│  │#       #│  │
│  │         │  │
│  │         │  │
│  │#       #│  │
│  │         │  │
│  │         │  │
│  │#       #│  │
│  └─────────┘ #│
│              6│
└───────────────┘
""",
    7: f"""
┌───────────────┐
│7              │
│# ┌─────────┐  │
│  │#       #│  │
│  │    #    │  │
│  │         │  │
│  │#       #│  │
│  │         │  │
│  │         │  │
│  │#       #│  │
│  └─────────┘ #│
│              7│
└───────────────┘
""",
    8: f"""
┌───────────────┐
│8              │
│# ┌─────────┐  │
│  │#       #│  │
│  │    #    │  │
│  │         │  │
│  │#       #│  │
│  │         │  │
│  │    #    │  │
│  │#       #│  │
│  └─────────┘ #│
│              8│
└───────────────┘
""",
    9: f"""
┌───────────────┐
│9              │
│# ┌─────────┐  │
│  │#       #│  │
│  │    #    │  │
│  │         │  │
│  │#   #   #│  │
│  │         │  │
│  │    #    │  │
│  │#       #│  │
│  └─────────┘ #│
│              9│
└───────────────┘
""",
    10: f"""
┌───────────────┐
│10             │
│# ┌─────────┐  │
│  │#       #│  │
│  │    #    │  │
│  │#       #│  │
│  │         │  │
│  │#       #│  │
│  │    #    │  │
│  │#       #│  │
│  └─────────┘ #│
│             10│
└───────────────┘
""",
    "J": f"""
┌───────────────┐
│J              │
│# ┌─────────┐  │
│  │#   ___  │  │
│  │   |_  | │  │
│  │     | | │  │
│  │  _  | | │  │
│  │ | |_' | │  │
│  │ `.___.' │  │
│  │        #│  │
│  └─────────┘ #│
│              J│
└───────────────┘
""",
    "Q": f"""
┌───────────────┐
│Q              │
│# ┌─────────┐  │
│  │#  ___   │  │
│  │  / _ \\  │  │
│  │ | | | | │  │
│  │ | | | | │  │
│  │ | | | | │  │
│  │  \\___\\_\\│  │
│  │        #│  │
│  └─────────┘ #│
│              Q│
└───────────────┘
""",
    "K": f"""
┌───────────────┐
│K              │
│# ┌─────────┐  │
│  │#  _  __ │  │
│  │  | |/ / │  │
│  │  | ' /  │  │
│  │  |  <   │  │
│  │  | . \\  │  │
│  │  |_|\\_\\ │  │
│  │        #│  │
│  └─────────┘ #│
│              K│
└───────────────┘
""",
    "A": f"""
┌───────────────┐
│A              │
│# ┌─────────┐  │
│  │         │  │
│  │         │  │
│  │         │  │
│  │    #    │  │
│  │         │  │
│  │         │  │
│  │         │  │
│  └─────────┘ #│
│              A│
└───────────────┘
""",
    "back": f"""
┌───────────────┐
│# # # # # # # #│
│ # # # # # # # │
│# # # # # # # #│
│ # # # # # # # │
│# # # # # # # #│
│ # # # # # # # │
│# # # # # # # #│
│ # # # # # # # │
│# # # # # # # #│
│ # # # # # # # │
│# # # # # # # #│
└───────────────┘
"""
}


if __name__ == "__main__":
    import time
    print(logo)
    for card in cards.values():
        print(card)
        time.sleep(0.5)