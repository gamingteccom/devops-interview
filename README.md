# Interview Project

## About the application

It is a simple application that we should build from the source code.

**How to build**: the command `python build.py` generates an `index.php` file and puts it in a public directory

## Task

Your task is to prepare the configuration necessary to deploy the `index.php` application to a Kubernetes cluster.

**NOTE**:

- Let's assume that Kubernetes cluster already exists and GitLab has permissions to it.
- For docker registry use GitLab Registry

### TODO

- Dockerfile was written some time ago by unknown person. Review it and fix if needed. Follow the best practices.
- We already have HELM chart for our app with `domain: my-app1.com`.
  But we want to add domains dynamically using `domains` variable (see example in chart values)
  Please update chart to provide required resources for every domain.

  ```shell
  # Render chart templates locally and display the output
  helm template .helm
  #
  # or using docker
  #
  docker run --rm -v $(pwd):/apps -w /apps alpine/helm template .helm
  ```

- Implement GitLab pipeline to build docker image, push it in registry and deploy it using helm chart
