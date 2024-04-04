def retrieve_permissions(permissions):
    return {
        role: {
            action: (action in action_list)
            for action in ['READ', 'CREATE', 'UPDATE', 'DELETE']
        }
        for role, action_list in permissions.items()
    }

EMPLOYEE_PERMISSIONS = retrieve_permissions({
    'management': ['READ', 'CREATE', 'UPDATE', 'DELETE'],
    'sales': ['READ'],
    'support': ['READ'],
})

CLIENT_PERMISSIONS = retrieve_permissions({
    'management': ['READ', 'CREATE', 'UPDATE', 'DELETE'],
    'sales': ['READ', 'CREATE'],
    'support': ['READ'],
})

CONTRACT_PERMISSIONS = retrieve_permissions({
    'management': ['READ', 'CREATE', 'UPDATE', 'DELETE'],
    'sales': ['READ', 'UPDATE'],
    'support': ['READ'],
})

EVENT_PERMISSIONS = retrieve_permissions({
    'management': ['READ', 'CREATE', 'UPDATE', 'DELETE'],
    'sales': ['READ'],
    'support': ['READ', 'UPDATE'],
})
