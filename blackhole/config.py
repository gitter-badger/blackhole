# -*- coding: utf-8 -*-
"""Configuration structure for Blackhole."""


import getpass
import grp
import inspect
import os
import pwd
import re

from blackhole.exceptions import ConfigException


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(object):
    """
    Configuration module for Blackhole.

    Default values are provided as well as self-test functionality
    to sanity check configuration.
    """

    __metaclass__ = Singleton
    config_file = None
    _address = '127.0.0.1'
    _port = 25
    _user = None
    _group = None
    _log_file = None
    _timeout = 60

    def __init__(self, config_file="/etc/blackhole.conf"):
        """
        Initialise the configuration.

        Set the default user and group to the current user and group from
        `getpass.getuser`.

        :param config_file: The configuration file.
        :type config_file: str
        """
        self.config_file = config_file
        self.user, self.group = getpass.getuser(), getpass.getuser()

    def load(self):
        """
        Load the configuration file and parse.

        Spaces, single and double quotes will be stripped. Lines beginning in
        # will be ignored.

        :returns: obj -- instance of `blackhole.config.Config`
        """
        if self.config_file is None:
            return self
        if not os.access(self.config_file, os.R_OK):
            raise IOError("Config file does not exist or is not readable.")
        for line in open(self.config_file, 'r').readlines():
            line = line.strip()
            if line.startswith('#'):
                continue
            try:
                key, value = line.split('=')
            except ValueError:
                continue
            key, value = key.strip(), value.strip()
            key = "_{}".format(key)
            value = value.replace('"', '').replace("'", '')
            if not getattr(self, key):
                continue
            setattr(self, key, value)
        return self

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self):
        return self._address

    @property
    def port(self):
        return int(self._port)

    @port.setter
    def port(self, value):
        self._port = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value

    @property
    def log_file(self):
        return self._log_file

    @log_file.setter
    def log_file(self, value):
        self._log_file = value

    @property
    def timeout(self):
        return int(self._timeout)

    @timeout.setter
    def timeout(self, value):
        self._timeout = value

    def self_test(self):
        """Test configuration validity.

        .. notes::

           Uses the magic of `inspect.getmembers` to introspect methods
           beginning with 'test_' and calling them.
        """
        members = inspect.getmembers(self, predicate=inspect.ismethod)
        for member in members:
            name, mcallable = member
            if name.startswith('test_'):
                mcallable()
        return self

    def test_address(self):
        """
        Validate IPv4 address format.

        :raises: `blackhole.exceptions.ConfigException`

        .. note::

           Classifies 'localhost' as a valid IPv4 address.
        """
        address = re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", self.address)
        if self.address not in ('localhost',) and not address:
            msg = "{} is not a valid IPv4 address".format(self.address)
            raise ConfigException(msg)

    def test_port(self):
        """
        Validate port number.

        :raises: `blackhole.exceptions.ConfigException`

        .. note::

           Only verifies port is a valid integer, does not verify port is
           available or not in use.
        """
        try:
            int(self.port)
        except ValueError:
            msg = "{} is not a valid port number".format(self.port)
            raise ConfigException(msg)

    def test_user(self):
        """
        Validate user exists in UNIX password database.

        :raises: `blackhole.exceptions.ConfigException`

        .. note::

           Defaults to `getpass.getuser` if no user is specified.
        """
        try:
            pwd.getpwnam(self.user)
        except ValueError:
            msg = "{} is not a valid user".format(self.user)
            raise ConfigException(msg)

    def test_group(self):
        """
        Validate group exists in UNIX group database.

        :raises: `blackhole.exceptions.ConfigException`

        .. note::

           Defaults to `getpass.getuser` if no group is specified. Assumes a
           group has been created with the same name as the user.
        """
        try:
            grp.getgrnam(self.group)
        except ValueError:
            msg = "{} is a not a valid group".format(self.group)
            raise ConfigException(msg)

    def test_log_file(self):
        """
        Validate log file and location are writable.

        :raises: `blackhole.exceptions.ConfigException`
        """
        if self.log_file is not None and not os.access(self.log_file, os.W_OK):
            msg = "Cannot open log file {} for writing".format(self.log_file)
            raise ConfigException(msg)

    def test_timeout(self):
        """
        Validate timeout - only allow a valid integer value in seconds.

        :raises: `blackhole.exceptions.ConfigException`
        """
        try:
            int(self.timeout)
        except ValueError:
            msg = "{} is not a valid number of seconds".format(self.timeout)
            raise ConfigException(msg)
