# Kubernetes Secret Generator

The aim of this program is to automate the process of creating a Kubernetes secret containing Docker credentials. It asks the user for the necessary information, such as the registry URL, namespace, username, and password, and generates a YAML file containing the secret that can be applied in a Kubernetes cluster.

## Documentation

To use this program, follow these steps:

1. Install Python 3 on your system.
2. Clone this repository to your local machine.
3. Open a terminal or command prompt and navigate to the directory where you cloned the repository.
4. Run the python `k8s-secret-generator.py` command to start the program.
5. Follow the prompts to enter the registry URL, namespace, username, and password.
6. The program will generate a YAML file named `secret.yaml` containing the Kubernetes secret.
7. Apply the secret in your Kubernetes cluster by running the `kubectl apply -f secret.yaml` command.

## Contributing

This program is open source and welcomes contributions from the community. If you have an idea for a new feature or a bug fix, please open a new issue or pull request in the repository. I will review your changes and, if they are in line with the project goals and meet the necessary quality standards, I will merge them into the main branch of the code.

Thank you for considering contributing to this project. Your efforts will help make it better and more useful to users who want to automate the process of creating Kubernetes secrets.