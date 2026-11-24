import os

ENTRY_TEXT = (
    "You've pitched me that app at every dinner for two years — tell it to the agent "
    "once tonight and you'll hand me the thing itself before dessert; no code, nothing "
    "to install, and if it's bad you've lost an evening, not the years."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
