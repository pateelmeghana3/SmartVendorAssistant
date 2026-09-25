from flask import Blueprint, render_template, request, redirect, session

from models.festival import (
    get_all_festivals,
    add_festival,
    delete_festival
)

festival_bp = Blueprint("festival", __name__)


# ==========================================================
# FESTIVAL PAGE
# ==========================================================

@festival_bp.route("/festival", methods=["GET", "POST"])
def festival():

    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":

        festival_name = request.form["festival_name"]
        festival_date = request.form["festival_date"]

        add_festival(festival_name, festival_date)

        return redirect("/festival")

    festivals = get_all_festivals()

    return render_template(
        "festival.html",
        festivals=festivals
    )


# ==========================================================
# DELETE FESTIVAL
# ==========================================================

@festival_bp.route("/delete_festival/<int:id>")
def remove_festival(id):

    if "user" not in session:
        return redirect("/login")

    delete_festival(id)

    return redirect("/festival")