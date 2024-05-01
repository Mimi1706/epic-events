def retrieve_permissions(permissions):
    return {
        role: {
            action: (action in action_list)
            for action in ["READ", "CREATE", "UPDATE", "DELETE"]
        }
        for role, action_list in permissions.items()
    }


EMPLOYEE_PERMISSIONS = retrieve_permissions(
    {
        "gestion": ["READ", "CREATE", "UPDATE", "DELETE"],
        "commercial": ["READ"],
        "support": ["READ"],
    }
)

CLIENT_PERMISSIONS = retrieve_permissions(
    {
        "gestion": ["READ", "CREATE", "UPDATE", "DELETE"],
        "commercial": ["READ", "CREATE"],
        "support": ["READ"],
    }
)

CONTRACT_PERMISSIONS = retrieve_permissions(
    {
        "gestion": ["READ", "CREATE", "UPDATE", "DELETE"],
        "commercial": ["READ", "UPDATE"],
        "support": ["READ"],
    }
)

EVENT_PERMISSIONS = retrieve_permissions(
    {
        "gestion": ["READ", "CREATE", "UPDATE", "DELETE"],
        "commercial": ["READ"],
        "support": ["READ", "UPDATE"],
    }
)
