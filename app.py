from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "mastermind_secret_key"


def generate_number(length):
    return "".join(str(random.randint(0, 9)) for _ in range(length))


def start_game(length=4):
    session["length"] = length
    session["secret_number"] = generate_number(length)
    session["attempts"] = 20
    session["history"] = []


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    # Start game first time
    if "secret_number" not in session:
        start_game()

    if request.method == "POST":

        # Difficulty selection
        if "difficulty" in request.form:

            level = request.form["difficulty"]

            if level == "easy":
                start_game(3)

            elif level == "hard":
                start_game(5)

            else:
                start_game(4)

            return redirect("/")


        # Guess submission
        guess = request.form.get("guess", "")

        if guess.isdigit() and len(guess) == session["length"]:

            if session["attempts"] > 0:

                session["attempts"] -= 1

                secret = session["secret_number"]

                if guess == secret:

                    used = 20 - session["attempts"]

                    if used <= 5:
                        medal = "🥇 Gold Master"
                    elif used <= 10:
                        medal = "🥈 Silver Solver"
                    else:
                        medal = "🥉 Bronze Breaker"


                    message = f"""
                    🎉 YOU WON!<br>
                    🏆 {medal}<br>
                    🔢 Secret Number: {secret}
                    """

                    # Reassign (not .append) so Flask detects the session change
                    session["history"] = session["history"] + [
                        f"{guess} → WIN 🎉"
                    ]

                    session["attempts"] = 0


                else:

                    result = []

                    for i in range(session["length"]):

                        if guess[i] == secret[i]:
                            result.append("🟩")

                        else:
                            result.append("⬜")


                    pattern = " ".join(result)

                    message = f"""
                    ❌ Wrong Guess<br>
                    Correct Positions: {pattern}
                    """

                    # Reassign (not .append) so Flask detects the session change
                    session["history"] = session["history"] + [
                        f"{guess} → {pattern}"
                    ]


            else:
                message = (
                    f"💀 Game Over! "
                    f"Number was {session['secret_number']}"
                )


        else:
            message = (
                f"Enter a valid {session['length']} digit number"
            )


    return render_template(
        "index.html",
        message=message,
        history=session["history"],
        attempts=session["attempts"],
        length=session["length"]
    )



@app.route("/play_again")
def play_again():

    session.clear()

    return redirect("/")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)