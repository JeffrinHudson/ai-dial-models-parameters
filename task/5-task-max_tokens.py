from task.app.main import run

run(
    deployment_name='gpt-4o',
    max_tokens=10,  # Limit the response to 10 tokens
    print_only_content=True,
)