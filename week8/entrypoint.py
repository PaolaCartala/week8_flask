from src.app import App

app = App.create_app()

if __name__ == '__main__':
    from src.db import db
    db.init_app(app)
    app.run(debug=True)
