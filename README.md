# Tiny Tiny Computer

A lightweight simulator built with Flet. This repository is pre-configured for seamless development using GitHub Codespaces. All dependencies and ports are already set up. Just follow the instructions below to get started.

---

## 🚀 Getting Started with Codespaces

This project is optimized for GitHub Codespaces, allowing you to quickly spin up a development environment without additional configuration.

### Steps to Create a Codespace

1. **Navigate to the Repository**:
   Go to the repository page on GitHub.

2. **Create a Codespace**:
   - Click on the green `Code` button.
   - Select the `Codespaces` tab.
   - Click `Create codespace on main`.

3. **Wait for Initialization**:
   - GitHub Codespaces will automatically build the development container.
   - All dependencies will be installed during the setup process.

---

## 🏃 Running the Application

Once the Codespace is ready:

1. **Open the Terminal**:
   - You can access the terminal by clicking on `Terminal > New Terminal` in the top menu.

2. **Run the Application**:
   - In the terminal, execute the following command:
     ```bash
     python3 run.py
     ```

3. **Access the Application**:
   - The application runs on port `8080` (already exposed in the Codespace).
   - Click on the `Ports` tab in the Codespaces interface and open the forwarded port in your browser.

---

## 🔧 Development Workflow

- **Pre-commit Hooks**: This repository uses `pre-commit` hooks for code formatting and linting (`black` and `isort`). All changes are automatically checked when committing code.
- **Dependencies**: Dependencies are managed using `pip` and are automatically installed when the Codespace is created.

---