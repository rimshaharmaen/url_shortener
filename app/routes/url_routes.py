from datetime import datetime
from flask import Blueprint, request, jsonify, redirect
import validators

from app import db
from app.models.url import URL
from app.utils.shortener import encode

url_bp = Blueprint("url_bp", __name__)


@url_bp.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json(silent=True) or {}
    long_url = data.get("long_url")

    if not long_url or not validators.url(long_url):
        return jsonify({"error": "A valid long_url is required"}), 400

    new_entry = URL(long_url=long_url, short_code="pending")
    db.session.add(new_entry)
    db.session.flush()

    new_entry.short_code = encode(new_entry.id)
    db.session.commit()

    return jsonify(new_entry.to_dict()), 201


@url_bp.route("/<short_code>", methods=["GET"])
def redirect_to_url(short_code):
    entry = URL.query.filter_by(short_code=short_code).first()

    if entry is None:
        return jsonify({"error": "Short URL not found"}), 404

    if entry.expires_at and entry.expires_at < datetime.utcnow():
        return jsonify({"error": "This link has expired"}), 410

    entry.click_count += 1
    db.session.commit()

    return redirect(entry.long_url)