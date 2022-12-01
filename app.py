from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'movies_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/')
def index():
    sql = '''INSERT INTO `movies_db`.`movies`  
            (`created_at`, 
            `updated_at`,
            `title`,
            `rating`,
            `awards`,
            `release_date`,
            `length`,
            `genre_id`)
            VALUES
            (
            null,
            null,
            'Pelicula 1',
            10.0,
            2,
            sysdate(),
            120,
            2);
    '''

    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

    return render_template('movies/index.html')


if __name__ == '__main__':
    app.run(debug=True)
