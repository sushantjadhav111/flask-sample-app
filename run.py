from app import create_app

app = create_app()
print("Server starting...,,running ")
if __name__ == "__main__":
    app.run(debug=True)