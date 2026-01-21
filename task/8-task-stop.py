from task.app.main import run

print("\n--- Using stop='\\n\\n' ---\n")
run(
    deployment_name='gpt-4o',
    stop="\n\n",  # Stop at double newline
    print_only_content=True,
)

print("\n--- Using stop=[\"**Embedding Layer**\", \"**Transformer Blocks**\", \"**Training**\"] ---\n")
run(
    deployment_name='gpt-4o',
    stop=["**Embedding Layer**", "**Transformer Blocks**", "**Training**"],  # Stop at any of these phrases
    print_only_content=True,
)

# Optional: See the full JSON response and finish_reason
print("\n--- Using stop='\\n\\n' with full response ---\n")
run(
    deployment_name='gpt-4o',
    stop="\n\n",
    print_only_content=False,
)