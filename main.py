import os


RANT = "At the public sink, the faucet dies mid-rinse, so I wave my soapy hands under it like a tiny helicopter trying to land. Apparently its CAPTCHA is just: prove you're human by flapping harder while the soap sets like grout."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(RANT)
    print(len(RANT))


if __name__ == "__main__":
    main()
