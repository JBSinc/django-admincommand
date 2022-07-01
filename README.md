# Django-AdminCommand 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


Django-AdminCommand is a Django application that makes it possible
to run Django management commands from the admin.

## Contributions

This is an enhanced fork, see the original repo: https://github.com/skorokithakis/django-admincommand

Starting from the fork, changes were made in the following area:

- Remove dependency on django-sneak
- Adding correct post-migrate signal for Permissions

## Dependencies

 - django-async (not mandatory): Used to make task asynchronous.


## Installation

For now you can only clone this repo and run `python setup.py develop` (sudo if needed) to setup Django AdminCommand.


## Settings


You need to activate the Django admin in the settings and ``urls.py``
depending on your needs the configuration may vary, refer
to the Django documentation related to the
[`admin application`](https://docs.djangoproject.com/en/dev/ref/contrib/admin/).

Don't forget to add the application where you defined management
commands in the list of installed applications. This might be already
done but it might not be the case if you use an application to gather
all the management commands that must be admin commands.


## Make magic happens


Create a Django Management Command::

```py
# ./music/management/commands/lyrics.py


class Command(BaseCommand):
    help = "Compute lyrics based an bitorological fluctuations"

    def handle(self, *args, **options):
        # algorithm that generated lyrics based on a title and a dictionary
```

Then you will have to create a configuration class for the command::

```py
# ./music/admincommands.py

from admincommand.models import AdminCommand


class Lyrics(AdminCommand):

    pass
```

*NOTE*: This all works based on naming conventions. The file with the form must be called `admincommands` and the form class name must be the same as the management command file name (with camel case converted to underscore notation).
(This will probably change to settings based property in upcoming days)

And all is well, the new admin command will be available under the
«Admin Command» area of the administration of the default admin site.

If you use custom admin site, don't forget to register
``admincommand.models.AdminCommand`` to the admin site object.


## Forms

Forms for the options are build by running an inspection of the command argument (default to bool / checkbox).
If the form does not seems correct for your management command, please check the `type` option in your management command.


## Logs

Logs emitted using the Django (and Python) logging module will be printed on the result page of the admin. They will still go into the normal logging process.


## Compatibility

This module was tested and is designed for Django 1.11, may work with other versions

## Permissions

You MUST add to every user or groups that should have access to the list of commands
«Can change admincommand» permission. Every admin command gets it's own permission
«Can Run AnAdminCommand», so you can add it to proper users or group. Users will
only see and be able to execute admin commands for which they have the permission.


## Asynchronous tasks

**This is not supported in this version**
