.. _configuration-file-example:

==========================
Configuration file example
==========================

You can download a copy of this example file from
`GitHub <https://github.com/kura/blackhole/blob/master/example.conf>`_.

.. code-block:: ini
   :linenos:

    #
    # Address to bind to.
    # Defaults to 127.0.0.1
    #
    # address=localhost
    # address=127.0.0.1
    address=0.0.0.0

    #
    # Port to use.
    # Defaults to 25
    port=25

    #
    # User to run blackhole as.
    # Defaults to current user.
    #
    # user=blackhole

    #
    # Group to run blackhole as.
    # Defaults to current group.
    #
    # group=blackhole

    #
    # Timeout after no data has been received in seconds.
    # Defaults to 60 seconds.
    #
    # timeout=45
    # timeout=300

    #
    # Port to use for TLS.
    # 465 is the recognised port for SMTPS
    #
    # tls_port=465

    #
    # TLS certificate location.
    # Certificate should be x509 format.
    #
    # tls_cert=/etc/ssl/blackhole.crt

    #
    # TLS key file for x509 certificate.
    #
    # tls_key=/etc/ssl/blackhole.key


    #
    # Delay for X seconds after the DATA command before sending the final
    # response.
    #
    # Must be less than timeout.
    # Time is in seconds.
    # Non-blocking - won't affect other connections.
    #
    # delay=10

    #
    # Response mode for the final response after the DATA command.
    #
    # accept (default) - all emails are accepted with 250 code.
    # bounce - bounce all emails with a random code.
    # random - randomly accept or bounce.
    #
    # Bounce codes:
    # 450: Requested mail action not taken: mailbox unavailable
    # 451: Requested action aborted: local error in processing
    # 452: Requested action not taken: insufficient system storage
    # 458: Unable to queue message
    # 521: Machine does not accept mail
    # 550: Requested action not taken: mailbox unavailable
    # 551: User not local
    # 552: Requested mail action aborted: exceeded storage allocation
    # 553: Requested action not taken: mailbox name not allowed
    # 571: Blocked
    #
    # mode=accept
