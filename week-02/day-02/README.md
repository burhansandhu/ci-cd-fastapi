# CI/CD with GitHub Actions

## Topics

### 1. GitHub Actions

- **Workflows & `.github/workflows`** — Workflows define automated processes, and their YAML files are stored inside `.github/workflows/`.
- **Events & Triggers** — Events such as pushes and pull requests can trigger workflows automatically.
- **Jobs & Steps** — Jobs contain groups of tasks, while steps are individual tasks executed within a job.
- **Runners** — Runners are the machines/environments that execute workflow jobs.
- **Actions & Marketplace Actions** — Reusable actions perform common tasks without requiring the workflow to implement everything manually.
- **Workflow Permissions** — Permissions control what a workflow is allowed to access or modify.
- **Secrets & Environment Variables** — Secrets securely store sensitive values, while environment variables provide configuration to workflows and jobs.
- **Job Dependencies** — Dependencies control the execution order between jobs using mechanisms such as `needs`.
- **Artifacts & Logs** — Artifacts preserve files produced by jobs, while logs show the output and execution details of workflow jobs.

### 2. CI Pipeline — Pull Request to `main`

The CI pipeline validates code before it is merged into the `main` branch.

- **Install dependencies** — Prepare the CI environment with the project's required dependencies.
- **Run linting** — Check the source code for formatting and code-quality issues.
- **Run tests** — Execute automated tests to detect functional problems.
- **Validate the application** — Ensure the application is in a valid and usable state before merging.

### 3. CI/CD Pipeline — Push to `main`

The CI/CD pipeline runs after changes are pushed to `main` and prepares the application for distribution.

- **Run tests** — Verify that the code passes automated tests.
- **Build Docker image** — Create a Docker image from the application and its Dockerfile.
- **Automatically generate/increment image tags** — Generate identifiable image versions automatically.
- **Authenticate with container registry** — Securely authenticate the workflow with the target container registry.
- **Push image to Docker Hub, AWS ECR, or Google GCR** — Publish the built Docker image to a container registry.

### 4. Docker & Image Versioning

- **Production Dockerfile** — Create a Dockerfile suitable for running the application in a production environment.
- **Image tagging** — Use tags to identify different versions of Docker images.
- **Automatic version generation** — Generate image versions automatically through the CI/CD pipeline.
- **Registry authentication** — Securely authenticate before pushing Docker images to a registry.
