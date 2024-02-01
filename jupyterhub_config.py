from jupyterhub.spawner import SimpleLocalProcessSpawner

## Class for authenticating users.
#  
#          This should be a subclass of :class:`jupyterhub.auth.Authenticator`
#  
#          with an :meth:`authenticate` method that:
#  
#          - is a coroutine (asyncio or tornado)
#          - returns username on success, None on failure
#          - takes two arguments: (handler, data),
#            where `handler` is the calling web.RequestHandler,
#            and `data` is the POST form data from the login page.
#  
#          .. versionchanged:: 1.0
#              authenticators may be registered via entry points,
#              e.g. `c.JupyterHub.authenticator_class = 'pam'`
#  
#  Currently installed: 
#    - default: jupyterhub.auth.PAMAuthenticator
#    - dummy: jupyterhub.auth.DummyAuthenticator
#    - null: jupyterhub.auth.NullAuthenticator
#    - pam: jupyterhub.auth.PAMAuthenticator
#  Default: 'jupyterhub.auth.PAMAuthenticator'
c.JupyterHub.authenticator_class = dummy

## Paths to search for jinja templates, before using the default templates.
#  Default: []
c.JupyterHub.template_paths = ['templates']

## Extra variables to be passed into jinja templates
#  Default: {}

c.JupyterHub.template_vars = c.JupyterHub.template_vars = {
    'custom': {
        "interface_selector": False,
        'org': {
            'name': 'NCAR',
            'logo_url': 'static/extra-assets/images/CISL-contemp-logo-blue.png',
            'url': 'https://ncar.ucar.edu/',
        },
        'operated_by': {
            'name': 'CISL',
            'url': 'https://www2.cisl.ucar.edu/',
            'custom_html': '',
        },
        'funded_by': {
            'name': 'NSF',
            'url': 'https://www.nsf.gov/',
            'custom_html': '',
        },
        'designed_by': {
            'name': 'CISL Cloud Pilot Team',
            'url': 'mailto:cisl-cloud-pilot@ucar.edu',
            'custom_html': '',
        }
    }
}

## Timeout (in seconds) before giving up on starting of single-user server.
#  
#  This is the timeout for start to return, not the timeout for the server to
#  respond. Callers of spawner.start will assume that startup has failed if it
#  takes longer than this. start should return when the server process is started
#  and its location is known.
#  Default: 60
c.Spawner.start_timeout = 3600
