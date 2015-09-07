# Flame for Django Suit

Solves two problems:

 - Warns users when two people are editing the same object. 
 - Autosaves the changes to firebase realtime and notifies the user if there are unsaved changes. 
 If the user leaves the page for some reason, they can see their unsaved changes and apply them to the form.
 
## The main problem

When two users are editing the same django admin page at the same time, it is almost inevitable that one of the users 
will will override the other's changes. 
Flame is the simplest solution to prevent this problem. 

## The solution

Use a pub-sub server to track active users and notify others when a change occurs.

![save-notification](/docs/images/save-notification.png)

## Autosave!

Many people use django for content editing purposes. The biggest nightmare for an editor is to accidentally 
close the browser and lose all his work. 
The modern web apps (Gmail, Google docs, etc...) already support auto-save and lack of this feature in sites built with django create a bad 
experience for the users.

#### No need to set-up Tornado or similar pub-sub server.

Flame uses Firebase as the pub-sub provider. Firebase is quite reliable and the free tier already supports up to 50 connections which should be enough for an admin page. 


### How it works?
Flame syncs the contents of the change form regularly with Firebase. When the user saves the form, it deletes this data from firebase.
However if the user leaves the page without saving the form, the unsaved data stays at the page. 
When the user re-enters to that page, he sees a notification box that says "You have unsaved changes" 
The user can choose to apply the changes to the form or ignore (and delete) this content forever.

# Setting-up

```
pip install django-suit-flame
```

Add suit_flame *before* django-suit into the INSTALLED_APPS setting

```
INSTALLED_APPS = (
    'suit_flame',
    'suit',
```


Create a new firebase database and add necessary keys to the settings.py:

```
FLAME_AUTOSAVE = True
FLAME_FIREBASE_SUBDOMAIN = 'https://example-subdomain-136.firebaseio.com'
FLAME_FIREBASE_SECRET_KEY = 'e22bA3KOg54gfwr9lmoWyi1sg8dL8uwOg8txRyfl2'
```

Make sure to make necessary security settings at firebase.

Go to your firebase project settings and update the Security & Rules section with these ones:

```
{
    "rules": {
        ".read": "auth != null",
        ".write": "auth != null"
    }
}
```

This will ensure the privacy of your contents.

# Contributors
 -  [Umit Dincel](https://github.com/umitdincel)
 -  [Yigit Guler](https://github.com/yigitguler)

Made by [Hipo](http://hipolabs.com)