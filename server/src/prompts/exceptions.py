class PromptNotFoundException(Exception):
    def __str__(self):
        return 'Prompt not found'
    

class NoParametersException(Exception):
    def __str__(self):
        return 'At least one field to change the prompt'


class PromptVarsExceptions(Exception):
    def __init__(self, vars: list = None):
        self.vars = vars
        self.message = 'Error'

    def __str__(self):
        return f'{self.message}: {self.vars}' if self.vars else self.message
        

class MissingPromptVariablesException(PromptVarsExceptions):
    def __init__(self, vars: list = None):
        super().__init__(vars)
        self.message = 'Missing variables'


class ExtraPromptVariablesException(PromptVarsExceptions):
    def __init__(self, vars: list = None):
        super().__init__(vars)
        self.message = 'Unexpected variables'


class SubException(Exception):
    pass

class PromptLimitReachedException(SubException):
    def __str__(self):
        return 'Prompt limit reached for your subscription'