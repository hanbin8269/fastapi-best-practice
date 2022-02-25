class User:
    def __init__(self, github_id: str, password: str, username: str):
        self.id = None
        self.github_id = github_id
        self.password = password
        self.username = username
        self.created_at = None
        self.updated_at = None
