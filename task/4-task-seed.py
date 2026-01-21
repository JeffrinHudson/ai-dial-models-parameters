from task.app.main import run

print("\n--- With seed=42 ---\n")
run(
    deployment_name='gpt-4o',
    seed=42,         # Set the seed for deterministic output
    n=5,             # Request 5 completions
    print_only_content=True,
)

print("\n--- Without seed (random output) ---\n")
run(
    deployment_name='gpt-4o',
    n=5,             # Request 5 completions, but no seed for randomness
    print_only_content=True,
)