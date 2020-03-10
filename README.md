
# Shopping list

I chose to do this project because it feels like the most useful for my development, as I was interested to learn or improve some of the concepts that are part of this project (i.e. user authentication, datastore interactions). I'll be able to apply what I learned to some personal projects of mine.


## Process
At first, I mostly followed along [this resource on setting up a Flask App app on with Google Cloud Appengine](https://cloud.google.com/appengine/docs/standard/python3/building-app/). And then I was tackling task by task.


## How to set up

Get the code here:
```
git clone https://github.com/KalindiFonda/shopping-list
```

In a separate folder create and activate the virtual environment:
```
python3 -m venv env
source env/bin/activate
```

From inside the project folder, install dependencies and then run the application:
```
pip install  -r requirements.txt
python main.py
```

To view app in the browser: [http://localhost:8080](http://localhost:8080).

---

Deploy app from root of project folder (same level as app.yaml):
```
gcloud app deploy
```

Check it out online:
```
gcloud app browse
```

#### Potential issues

Had some problems with the datastore indexes, that got solved by running the datastore emulator: https://cloud.google.com/datastore/docs/tools/datastore-emulator

A lot of `pip3 install module_is_missing` along the way.

### Done
[x] User can sign in with Google account
[x] lists persists across sign ins
[x] add item
[x] delete item
[x] delete all
[x] some comments, code clean up
[x] mini styling
[x] README 💪



### Wishlist

Code:
[ ] consolidate fetch items
[ ] input validation solution (so that <> don't mess up the delete call)
[ ] code currently verifies the token on each page load. [Cache results in an encrypted session store](http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
[ ] code modularity and structure
[ ] more readme

Usability:
[ ] user can add lists without being signed in, but needs to sign in to save.
[ ] add info to db + page without refreshing the page
[ ] "Expired token" message sometimes pops up

Features:
[ ] make shopping lists (i.e. favourite, add usual purchases with one click)
[ ] quantities

Style:
[ ] phone view, put user info on bottom
[ ] make a little pretty