class DomainError(Exception):
    pass

class ValidationError(DomainError):
    pass

class InfrastructureError(Exception):
    pass

class DuplicateExternalIdError(Exception):
    pass
