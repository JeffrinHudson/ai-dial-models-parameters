from task.app.main import run

# Try several temperature values in the valid range (0.0 to 1.0)
temperatures = [0.0, 0.5, 1.0]

for temp in temperatures:
    print(f"\n--- Testing temperature={temp} ---\n")
    run(
        deployment_name='gpt-4o',
        temperature=temp,
        print_only_content=True,
    )

# (Optional) Try an out-of-range value (2.1) to see what happens
print("\n--- Testing temperature=2.1 (optional, may cause error or fallback to max allowed) ---\n")
run(
    deployment_name='gpt-4o',
    temperature=2.1,
    print_only_content=True,
)