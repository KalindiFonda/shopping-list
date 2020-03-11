
# Shopping list

I chose to do this project because it feels like the most useful for my development, as I was interested to learn and deepen my knowledge on some of the concepts that are part of this project (i.e. user authentication, datastore interactions). I'll also be able to apply what I learned to some personal projects of mine (past and future).


## Process
At first, I mostly followed [this resource on setting up a Flask App app with Google Cloud Appengine](https://cloud.google.com/appengine/docs/standard/python3/building-app/). And then I was tackling task by task.

## How to set up

Get the code here:
```
git clone https://github.com/KalindiFonda/shopping-list
```

In a separate folder, create and activate the virtual environment:
```
python3 -m venv env
source env/bin/activate
```

From inside the project folder, install dependencies and then run the application:
```
pip install  -r requirements.txt
python main.py
```

To view the app in the browser: [http://localhost:8080](http://localhost:8080).

---

Deploy app from the root of the project folder (same directory level as app.yaml):
```
gcloud app deploy
```

Check it out online:
```
gcloud app browse
```

#### Potential issues

Had some problems with the datastore indexes that were solved by running the datastore emulator: https://cloud.google.com/datastore/docs/tools/datastore-emulator

A lot of `pip3 install module_is_missing` along the way.

### Done
- [x] User can sign in with Google account.
- [x] Lists persist across sign ins.
- [x] Add item to list.
- [x] Delete item from list.
- [x] Delete all.
- [x] Some comments, code clean up.
- [x] Mini styling.
- [x] README 💪.



### Wishlist

Code:
- [ ] Consolidate fetch items.
- [ ] Input validation solution (so that <> don't mess up the delete call).
- [ ] Code currently verifies the token on each page load. [Cache results in an encrypted session store](http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
- [ ] Code modularity and structure.
- [ ] More readme.

Usability:
- [ ] User can add lists without being signed in, but needs to sign in to save.
- [ ] Add info to db + page without refreshing the page.
- [ ] "Expired token" message sometimes pops up.

Features:
- [ ] Make shopping lists (i.e. favourite, add usual purchases with one click)
- [ ] Add quantities.

Style:
- [ ] Phone view, put user info on bottom.
- [ ] Make a little pretty.