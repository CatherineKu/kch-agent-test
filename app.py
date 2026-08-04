from veadk import Agent
from veadk.integrations.agentkit import create_agentkit_app, run_agentkit_app

root_agent = Agent(
    name="github_cicd_demo",
    description="A minimal demo agent for GitHub CI/CD.",
    instruction="You are a concise demo assistant.",
)

app = create_agentkit_app(
    root_agent,
    {"github_cicd_demo": "github_cicd_demo"},
    enable_feishu=False,
)

if __name__ == "__main__":
    run_agentkit_app(app)
