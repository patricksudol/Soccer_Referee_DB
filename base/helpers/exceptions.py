class DryRunException(Exception):
    """Database changes should be rolled back"""

    def __init__(self, message=''):
        if not message:
            message = 'Rolling back changes.'
        super(DryRunException, self).__init__(message)
