import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from google.auth.transport import requests
from google.cloud import datastore
import google.oauth2.id_token

firebase_request_adapter = requests.Request()
datastore_client = datastore.Client()

app = Flask(__name__)
app.secret_key = "super secret key"

# Store new item
def store_item(email, dt, item_name):
    entity = datastore.Entity(key=datastore_client.key('User', email, 'visit'))
    entity.update({
        'timestamp': dt,
        'item_name' : item_name
    })
    datastore_client.put(entity)
    flash('%s successfully added' % item_name, 'success')

# get all the items to display
def fetch_items(email):
    ancestor = datastore_client.key('User', email)
    query = datastore_client.query(kind='visit', ancestor=ancestor)
    query.order = ['-timestamp']
    items = query.fetch()
    return items

# delete item
@app.route('/delete/<int:item>/<string:name>/', methods=['POST'])
def delete(item, name):
    id_token = request.cookies.get('token')
    if id_token:
        claims = google.oauth2.id_token.verify_firebase_token(
                id_token, firebase_request_adapter)
        key = datastore_client.key('User',claims['email'],'visit', item)
        datastore_client.delete(key)
        flash('%s successfully deleted' % name, 'deleted')
    return redirect(url_for('root'))

# Delete whole shopping list
@app.route('/delete_list/', methods=['POST'])
def delete_list():
    id_token = request.cookies.get('token')
    if id_token:
        claims = google.oauth2.id_token.verify_firebase_token(
                id_token, firebase_request_adapter)
        ancestor = datastore_client.key('User', claims['email'])
        query = datastore_client.query(kind='visit', ancestor=ancestor)
        items = query.fetch()
        for item in items:
            key = datastore_client.key('User',claims['email'],'visit', item.id)
            datastore_client.delete(key)
        flash('Shopping list successfully deleted', 'deleted')
    return redirect(url_for('root'))


# main page loading info
@app.route('/', methods=[ 'GET', 'POST'])
def root():
    # Verify Firebase auth.
    id_token = request.cookies.get('token')
    error_message = None
    claims = None
    items = None
    # Check if there is a valid user
    if id_token:
        try:
            # Verify the token against the Firebase Auth API.
            claims = google.oauth2.id_token.verify_firebase_token(
                id_token, firebase_request_adapter)
            items = fetch_items(claims['email'])
        except ValueError as exc:
            # This will be raised if the token is expired or any other
            # verification checks fail.
            error_message = str(exc)
    # Serve page
    if request.method == "GET":
        return render_template('index.html',
            user_data=claims, error_message=error_message, items=items)
    # Add new entity and redirect to the above.
    elif request.method == "POST":
        item_name = request.form['shop-item']
        store_item(claims['email'], datetime.datetime.now(), item_name)
        return redirect(url_for('root'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
