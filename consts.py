import string

char_to_num = {
    val: str(key) for key, val in enumerate(string.digits + string.ascii_uppercase)
}
