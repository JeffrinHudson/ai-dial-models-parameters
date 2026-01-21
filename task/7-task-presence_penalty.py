from task.app.main import run

penalties = [-2.0, 0.0, 2.0]

for penalty in penalties:
    print(f"\n--- Testing presence_penalty={penalty} ---\n")
    run(
        deployment_name='gpt-4o',
        presence_penalty=penalty,
        print_only_content=True,
    )