from fast import app

if __name__ == '__main__':
    app.secret_key = 'xyzfhkfld'
    app.run(debug=True)