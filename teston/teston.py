import apps
app = apps.create_app('../config.py')

if __name__ == '__main__':
    app.run()
