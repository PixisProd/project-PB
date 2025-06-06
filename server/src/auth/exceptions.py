class UserAlreadyExistsException(Exception):
    def __str__(self):
        return 'A user with such data already exists'
    
class UserNotFoundException(Exception):
    def __str__(self):
        return 'User not found'

class IncorrectCredentialsException(Exception):
    def __str__(self):
        return 'Incorrect login or password'
    
class DeactivatedUserException(Exception):
    def __str__(self):
        return 'User deactivated'
    
class TokenException(Exception):
    pass

class ExpiredAccessTokenException(TokenException):
    def __str__(self):
        return 'Access token expired'

class ExpiredRefreshTokenException(TokenException):
    def __str__(self):
        return 'Refresh token expired'

class InvalidAccessTokenException(TokenException):
    def __str__(self):
        return 'Invalid access token'
    
class InvalidRefreshTokenException(TokenException):
    def __str__(self):
        return 'Invalid refresh token'
    
class MissingAccessTokenException(TokenException):
    def __str__(self):
        return 'Missing access token'
    
class MissingRefreshTokenException(TokenException):
    def __str__(self):
        return 'Missing refresh token'