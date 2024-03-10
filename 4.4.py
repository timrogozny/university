def fourth():
    ticket = input("Enter ticket number:")
    if len(ticket) % 2 == 1:
        print("Enter an odd ticket number!")
        return False
    half = len(ticket) // 2
    half1 = ticket[:half]
    half2 = ticket[half:]
    s = sum(map(int, half1))
    s2 = sum(map(int, half2))
    if s == s2:
        print("Your ticket is lucky!!!")
    else:
        print("Sad( Your ticket isnt lucky.")

fourth()