class PromptNotFoundException(Exception):
    def __str__(self):
        return 'Prompt not found'