import random

# level key: (name, max number, attempts allowed, scans allowed)
LEVELS = {
    "1": ("Rookie Hacker", 50, 8, 2),
    "2": ("Pro Hacker", 100, 7, 1),
    "3": ("Elite Hacker", 500, 9, 1),
}

BANNER = r"""
 ============================================
   V A U L T   C R A C K E R
   Guess the secret access code before the
   security system locks you out!
 ============================================
"""


def ask(prompt):
    """Read input; exit cleanly if no more input is available (e.g. online compilers)."""
    try:
        return input(prompt)
    except EOFError:
        print("\n\nNo more input available. Exiting game.")
        raise SystemExit


def heat(guess, secret, top):
    """Return a 'temperature' hint based on how close the guess is."""
    gap = abs(guess - secret) / top * 100
    if gap <= 2:
        return "BURNING HOT"
    if gap <= 5:
        return "Hot"
    if gap <= 10:
        return "Warm"
    if gap <= 25:
        return "Cold"
    return "Freezing"


def scan_clue(secret, top, used):
    """Give one new clue about the secret code (each clue only once)."""
    clues = {
        "parity": f"The code is {'EVEN' if secret % 2 == 0 else 'ODD'}.",
        "div3": f"The code is {'' if secret % 3 == 0 else 'NOT '}divisible by 3.",
        "digits": f"The digits of the code add up to {sum(map(int, str(secret)))}.",
        "half": f"The code is in the {'LOWER' if secret <= top // 2 else 'UPPER'} half of the range.",
    }
    left = [k for k in clues if k not in used]
    if not left:
        return None
    pick = random.choice(left)
    used.add(pick)
    return clues[pick]


def play_round(level):
    name, top, max_tries, scans_left = LEVELS[level]
    secret = random.randint(1, top)
    attempts = 0
    scans_used = 0
    used_clues = set()

    print(f"\nLevel: {name}")
    print(f"Code range: 1 to {top} | Attempts: {max_tries} | Scans: {scans_left}")
    print("Type a number to guess, or 'scan' to use a scan for a clue.")

    while attempts < max_tries:
        left = max_tries - attempts
        raw = ask(f"\n[{left} attempt(s) left] Enter code: ").strip().lower()

        if raw == "scan":
            if scans_left == 0:
                print("No scans left!")
            else:
                clue = scan_clue(secret, top, used_clues)
                if clue is None:
                    print("The scanner has nothing more to reveal.")
                else:
                    scans_left -= 1
                    scans_used += 1
                    print(f"SCAN RESULT: {clue}  ({scans_left} scan(s) left)")
            continue

        if not raw.isdigit():
            print("Invalid input. Enter a whole number or 'scan'.")
            continue

        guess = int(raw)
        if guess < 1 or guess > top:
            print(f"Code must be between 1 and {top}.")
            continue

        attempts += 1

        if guess == secret:
            score = max(0, 1000 - 100 * (attempts - 1) - 150 * scans_used)
            print(f"\nACCESS GRANTED! Vault cracked in {attempts} attempt(s).")
            print(f"Score for this round: {score}")
            return True, attempts, score

        direction = "too LOW" if guess < secret else "too HIGH"
        print(f"Access denied. {guess} is {direction}. Heat: {heat(guess, secret, top)}")

    print(f"\nLOCKED OUT! The code was {secret}.")
    return False, attempts, 0


def choose_level():
    while True:
        print("\nChoose difficulty:")
        for key, (name, top, tries, scans) in LEVELS.items():
            print(f"  {key}. {name}  (1-{top}, {tries} attempts, {scans} scan(s))")
        choice = ask("Level: ").strip()
        if choice in LEVELS:
            return choice
        print("Pick 1, 2 or 3.")


def main():
    print(BANNER)
    rounds = wins = total_score = 0
    total_attempts = 0
    best = None

    while True:
        level = choose_level()
        won, attempts, score = play_round(level)

        rounds += 1
        total_attempts += attempts
        total_score += score
        if won:
            wins += 1
            if best is None or attempts < best:
                best = attempts

        print("\n--- Stats ---")
        print(f"Rounds: {rounds} | Cracked: {wins} | Total attempts: {total_attempts}")
        print(f"Total score: {total_score} | Fewest attempts in a win: {best if best else '-'}")

        if ask("\nHack another vault? (y/n): ").strip().lower() != "y":
            print(f"\nFinal score: {total_score}. Logging off...")
            break


if __name__ == "__main__":
    main()