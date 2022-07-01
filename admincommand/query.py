from django.conf import settings

from admincommand.models import AdminCommand


class ListQuerySet(object):
    """This is duck class behaving like a Django QuerySet"""

    def filter(self, *args, **kwargs):
        return self

    def order_by(self, *args, **kwargs):
        return self

    def delete(self):
        return len(self.value)

    class query:
        select_related = True
        where = False
        order_by = []

    def __init__(self, value=None):
        if value is None:
            self.value = []
        else:
            self.value = value

    def count(self):
        return len(self)

    def iterator(self):
        for v in self.value:
            yield v

    def _clone(self):
        return type(self)(list(self.value))

    def __len__(self):
        return len(self.value)

    def __getitem__(self, s):
        if isinstance(s, slice):
            return self.value.__getitem__(s)
        else:
            return self.value[s]


class CommandQuerySet(ListQuerySet):
    """
    Custom QuerySet to list runnable commands
    """

    def __init__(self, user, value=None):
        self.user = user
        if value is None:
            self.value = self.filter().value
        else:
            self.value = value

    def _clone(self):
        return type(self)(self.user, self.value)

    def filter(self, *args, **kwargs):
        all_commands = []

        for command in AdminCommand.all():
            # only list commands that the user can run to avoid useless messages
            full_permission_codename = "admincommand.%s" % command.permission_codename()
            if self.user.has_perm(full_permission_codename):
                all_commands.append(command)

        return type(self)(self.user, all_commands)
