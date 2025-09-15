# Contributing to NYC Taxi Data Enrichment Pipeline

Thank you for your interest in contributing to the NYC Taxi Data Enrichment Pipeline project! This document provides guidelines and information for contributors.

## How to Contribute

### 1. Fork the Repository
- Fork this repository on GitHub
- Clone your fork locally
- Create a new branch for your feature or bug fix

### 2. Development Setup
```bash
# Clone your fork
git clone https://github.com/your-username/ny-yellowcab-advanced.git
cd ny-yellowcab-advanced

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### 3. Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused on single responsibilities

### 4. Testing
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_validate_curated.py

# Run with coverage
pytest --cov=scripts --cov-report=html
```

### 5. Documentation
- Update README.md for any new features
- Add docstrings to new functions
- Update requirements.txt if new dependencies are added

### 6. Pull Request Process
1. Ensure all tests pass
2. Update documentation if needed
3. Write a clear PR description
4. Reference any related issues
5. Wait for review and address feedback

## Development Workflow

### Feature Development
1. Create a feature branch: `git checkout -b feature/new-feature`
2. Make your changes
3. Write tests for new functionality
4. Ensure all tests pass
5. Update documentation
6. Commit your changes
7. Push to your fork
8. Create a Pull Request

### Bug Fixes
1. Create a bug fix branch: `git checkout -b fix/bug-description`
2. Reproduce the bug
3. Write a test that fails due to the bug
4. Fix the bug
5. Ensure the test now passes
6. Update documentation if needed

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help newcomers learn and contribute
- Maintain professional communication

## Areas for Contribution

### High Priority
- Performance optimizations
- Additional visualization types
- Enhanced data validation
- Documentation improvements

### Medium Priority
- New feature engineering techniques
- Alternative data sources integration
- Web interface development
- API development

### Future Enhancements
- Machine learning model integration
- Real-time data processing
- Cloud deployment options
- Multi-language support

## Getting Help

- Check existing issues and documentation
- Create a new issue for bugs or feature requests
- Join discussions in pull request comments

Thank you for contributing to make this project better! 🚀