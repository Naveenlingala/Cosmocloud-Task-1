list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


# This function is designed to be easily extended and reused.
def merge_lists(list, updated_list):
    # iterate through list
    for items in list:
        id = items['id']
        if id in updated_list:
            # Update the Dictionary if exist
            for key, value in items.items():
                updated_list[id][key] = value
        else:
            # Create new dict
            updated_list[id] = items

    return updated_list


updated_list = merge_lists(list_1, {})
updated_list = merge_lists(list_2, updated_list)

print(list(updated_list.values()))
