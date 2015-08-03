# Flame for Django Suit

Solves two problems:

 - Warn users when two people are editing the same page. 
 - Autosave changes to the pub-sub server realtime and notify the user if there are unsaved changes.
 
## The main problem

When two users are editing the same django admin page at the same time, it is almost inevitable that one of the users will will override the other’s changes. 
Flame is the simplest solution to prevent this problem.

## The solution

Use a pub-sub server to track active users and notify others when a change occurs.

### No need to set-up Tornado or similar pub-sub server.

Flame uses Firebase as the pub-sub provider. Firebase is quite reliable and the free tier already supports 50 max connections. Which should be enough for an admin page. Other packages are also very convenient when compared to opeate a separate pub-sub server for this purpose.

# Setting-up

pip install django-suit-flame

add django-suit-flame *below* django-suit

add necessary firebase keys:

FLAME_FIREBASE_SUBDOMAIN = ""
FLAME_FIREBASE_SECRET_KEY = ""

### Additional settings

If you want to stop the autosave functionality, change this setting
FLAME_AUTOSAVE = True

# Other Features
## Autosave!

Many people are using django as CMS or content editing purposes. The biggest nightmare for an editor is to accidentally close the browser and lose all the data he wrote. 
The modern web apps (Gmail, Google docs, etc...) already support auto-save and many users complaint and suffer from this missing feature with sites built with django.

### How it works?
Flame syncs the contents of the change form regularly with the Firebase database. When the user saves the form, it deletes this data from firebase.
However if the user lefts the page without saving the form, the data stays at the page. 
When a user re-enters to that page, he sees a notification box that says "You have unsaved changes" 
The user can choose to apply the changes to the form or ignore (and delete) this content forever.


# Settings
# AUTOSAVE 


Made by Hipo