commands = {
    "switch_default_subscription": [
        ("az_data_command", "account list"),
        ("filter", lambda x: {k: v for k, v in x.items() if k in ['name']}),
        ("menu", "name"),
        ("az_set_command", "account set --subscription {name}")
    ]
}
# TODO: make definitions for more common taks here