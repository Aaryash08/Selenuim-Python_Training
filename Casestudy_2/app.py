from flask import Flask, request, jsonify

app = Flask(__name__)

movies = []
bookings = []

# GET all movies
@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200

# GET movie by ID
@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404

# POST add new movie
@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.json
    movies.append(data)
    return jsonify(data), 201

# PUT update movie
@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(request.json)
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404

# DELETE movie
@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted"}), 200
    return jsonify({"error": "Movie not found"}), 404

# POST booking
@app.route("/api/bookings", methods=["POST"])
def book_ticket():
    data = request.json
    if not data.get("movie_id") or not data.get("seats"):
        return jsonify({"error": "Invalid booking"}), 400
    bookings.append(data)
    return jsonify({"message": "Booking successful"}), 201

if __name__ == "__main__":
    app.run(debug=True)
