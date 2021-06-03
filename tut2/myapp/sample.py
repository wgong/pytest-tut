def validate_age(age):
    if age < 0:
        msg = "Age cannot be less than 0"
        print(f"age={age}: {msg}")
        raise ValueError("Age cannot be less than 0")
    else:
        print(f"age must be positive")
        return True
