from flask import Flask, render_template, request

app = Flask(__name__)


def convert_to_roman(number):
    roman_numbers = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""

    for value, symbol in roman_numbers:
        while number >= value:
            result = result + symbol
            number = number - value

    return result


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        user_input = request.form["number"]

        try:
            number = int(user_input)

            if 1 <= number <= 3999:

                roman_number = convert_to_roman(number)

                return render_template(
                    "result.html",
                    number_decimal=number,
                    number_roman=roman_number,
                    developer_name="Sumathi"
                )

            else:
                return render_template(
                    "index.html",
                    not_valid=True,
                    developer_name="Sumathi"
                )

        except ValueError:
            return render_template(
                "index.html",
                not_valid=True,
                developer_name="Sumathi"
            )

    return render_template(
        "index.html",
        not_valid=False,
        developer_name="Sumathi"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)