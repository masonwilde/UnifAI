# The top level file for the project. This file is responsible for running the
# main loop of the agent.

import config
import agent


def init_agent(config):
    my_agent = agent.Agent(config)
    return my_agent


def main():
    """The main loop of the agent."""
    cfg = config.Config("UnifAI", True, True, False)
    my_agent = init_agent(cfg)
    # TODO: Move to an agent Run method.
    while True:
        prompt = input("Prompt: ")
        # TODO: Hacky as all hell. Fix this.
        if prompt == "exit":
            print("Exiting...")
            break
        elif prompt.startswith("img"):
            print(my_agent.prompt_tti(prompt[3:]))
        else:
            print(my_agent.prompt_ttt(prompt))


if __name__ == "__main__":
    main()
