# Flame for Django Suit

Solves two problems:

 - Warns users when two people are editing the same object in the Django admin. 
 - Autosaves the changes to firebase in real time and notifies the user if there are unsaved changes. 
 If the user leaves the page for some reason, they can see their unsaved changes and apply them to the form.
 
## The main problem

When two users are editing the same Django admin page at the same time, it is almost 
inevitable that one of the users will override the other’s changes. 

Flame is the simplest solution to prevent this problem. 

## The solution

Use a pub-sub server to track active users and notify others when a change occurs.

![save-notification](/docs/images/save-notification.png)

## Autosave!

Many people use Django for content editing purposes. The biggest nightmare for an editor is to accidentally 
close the browser and lose all his work. 

Modern web apps (Gmail, Google docs, etc.) already support autosave and lack of this feature in sites built with Django create a bad experience for the users.

#### No need to setup Tornado or a similar pubsub server.

Flame uses Firebase as the pubsub provider. Firebase is quite reliable and the free tier already supports up to 50 connections which should be enough for an admin site. 

### How does it work?

Flame syncs the contents of the change form regularly with Firebase. When the user saves the form, it deletes this data from Firebase.

However if the user leaves the page without saving the form, the unsaved data stays in the Firebase data store. 

When the user reloads that page, he sees a notification box that says "You have unsaved changes." The user can choose to apply the changes to the form or ignore (and delete) this content forever.


# Setting up

```
pip install django-suit-flame
```

Add suit_flame *before* django-suit into the INSTALLED_APPS setting

```
INSTALLED_APPS = (
    'suit_flame',
    'suit',
```

Create a new Firebase data store and add necessary keys to settings.py:

```
FLAME_AUTOSAVE = True
FLAME_FIREBASE_SUBDOMAIN = 'https://example-subdomain-136.firebaseio.com'
FLAME_FIREBASE_SECRET_KEY = 'e22bA3KOg54gfwr9lmoWyi1sg8dL8uwOg8txRyfl2'
```

Make sure to add necessary security settings at Firebase.

Go to your Firebase project settings and update the Security & Rules section with these ones:

```
{
    "rules": {
        ".read": "auth != null",
        ".write": "auth != null"
    }
}
```

This will ensure the privacy of your data.


# Contributors

 -  [Umit Dincel](https://github.com/umitdincel)
 -  [Yigit Guler](https://github.com/yigitguler)

Made by [Hipo](http://hipolabs.com)
