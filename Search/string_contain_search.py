def is_part(some_string, target):
    if target:
        target_len = len(target)
        for i in range(len(some_string)):
            if some_string[i:i+target_len] == target:
                return True
    return False
