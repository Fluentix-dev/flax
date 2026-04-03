class Role:
    def __init__(self, roleName: str, roleDescription: str, roleId: str):
        self.name = roleName
        self.description = roleDescription
        self.id = roleId

    def __repr__(self):
        return f"<Role><name>{self.name}</><description>{self.description}</><id>{self.id}</></>"