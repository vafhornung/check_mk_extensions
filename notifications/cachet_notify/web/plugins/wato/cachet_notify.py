#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# (c) 2018 Heinlein Support GmbH
#          Robert Sander <r.sander@heinlein-support.de>

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

register_notification_parameters("cachet_notify", Dictionary(
    help = _("The Cachet component name is taken from the contact alias."),
    optional_keys = ['incident_prefix', 'incident_visible'],
    elements = [
        ("cachet_url", HTTPUrl(
            title = _("Cachet Server URL"),
            allow_empty = False,
        )),
        ("api_key", TextAscii(
            title = _("Cachet API Key"),
            help = _("You need to provide a valid API key to be able to send notifications."),
            allow_empty = False,
        )),
        ("incident_prefix", TextAscii(
            title = _("Cachet Incident Prefix"),
            allow_empty = True,
        )),
        ("incident_visible", Checkbox(
            title = _("Cachet Incident Visibility"),
            label = _('Visibility'),
            default_value = True,
            help = _("If set to 'on' (the default), incident reports will be visible in Cachet."),
        )),
    ]
))
