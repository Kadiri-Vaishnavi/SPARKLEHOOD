from flask import Flask, request, jsonify
from models import db, Incident

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/incidents", methods=["GET"])
def get_incidents():
    incidents = Incident.query.all()
    return jsonify([{
        "id": i.id,
        "title": i.title,
        "description": i.description,
        "severity": i.severity,
        "reported_at": i.reported_at.isoformat()
    } for i in incidents]), 200

@app.route("/incidents", methods=["POST"])
def create_incident():
    data = request.get_json()
    if not all(k in data for k in ("title", "description", "severity")):
        return jsonify({"error": "Missing required fields"}), 400

    if data["severity"] not in ["Low", "Medium", "High"]:
        return jsonify({"error": "Invalid severity level"}), 400

    incident = Incident(
        title=data["title"],
        description=data["description"],
        severity=data["severity"]
    )
    db.session.add(incident)
    db.session.commit()
    return jsonify({
        "id": incident.id,
        "title": incident.title,
        "description": incident.description,
        "severity": incident.severity,
        "reported_at": incident.reported_at.isoformat()
    }), 201

@app.route("/incidents/<int:id>", methods=["GET"])
def get_incident(id):
    incident = Incident.query.get(id)
    if not incident:
        return jsonify({"error": "Incident not found"}), 404

    return jsonify({
        "id": incident.id,
        "title": incident.title,
        "description": incident.description,
        "severity": incident.severity,
        "reported_at": incident.reported_at.isoformat()
    }), 200

@app.route("/incidents/<int:id>", methods=["DELETE"])
def delete_incident(id):
    incident = Incident.query.get(id)
    if not incident:
        return jsonify({"error": "Incident not found"}), 404

    db.session.delete(incident)
    db.session.commit()
    return jsonify({"message": "Incident deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
