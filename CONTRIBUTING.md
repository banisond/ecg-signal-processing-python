# Contributing to Biomedical ECG Starter Kit

First off, thank you for your interest in contributing! Whether it's bug fixes, algorithm improvements, documentation enhancements, or new signal processing features, all contributions are welcome.

To ensure a smooth collaboration process, please follow these guidelines when contributing to the project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful, constructive, and inclusive environment for all contributors.

## How Can I Contribute?

### 1. Reporting Bugs

If you find a bug in the filtering, peak detection, or API serialization, please open an issue on GitHub. Include:

* A clear description of the issue.

* Steps to reproduce the bug.

* Sample data or signal characteristics if applicable.

### 2. Suggesting Enhancements

Have an idea for a new feature (e.g., Pan-Tompkins algorithm support, frequency-domain HRV metrics like LF/HF, or multi-lead support)? Open an issue to discuss your proposal before jumping into code.

### 3. Pull Requests (PRs)

1. **Fork the repository** and clone your fork locally.

2. **Create a new branch** for your feature or bug fix:

   ```
   git checkout -b feature/ooohh-amazing-feature
   
   ```

3. **Set up your local environment**:

   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   
   ```

4. **Make your changes** and ensure all tests pass. Run the test script against your changes:

   ```
   pytest
   
   ```

5. **Commit your changes** using clear commit messages (e.g., `feat: add frequency-domain HRV calculations` or `fix: handle edge case in peak thresholding`).

6. **Push to your fork** and open a Pull Request against the `main` branch.

## Development Guidelines

* **Python Standards:** Write clean, readable Python code adhering to standard PEP 8 style conventions.

* **Serialization Safety:** Ensure all NumPy arrays and scalar types (`np.int64`, `np.float64`) are explicitly cast to native Python types (`int`, `float`) or lists before returning JSON responses from FastAPI endpoints.

* **Keep Dependencies Lean:** Avoid adding heavy external libraries unless strictly necessary for core signal processing.

Thank you for helping make open-source health-tech tooling better!