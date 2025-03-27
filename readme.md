# DmindChatbot

Fastapi backend for Dmind chatbot

## Installation

Follow these steps to set up the project:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Unix or MacOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Generating requirements.txt

To create or update the `requirements.txt` file with the current project dependencies, use the following command:

```bash
pip freeze > requirements.txt
```

This command will list all installed packages in your virtual environment and write them to the `requirements.txt` file. Make sure to run this command whenever you add or update dependencies in your project.

## Running the Application

To run the application:

```bash
uvicorn app.main:app --reload
```

This command starts the Uvicorn server with hot-reloading enabled, which is useful for development.

## Project Structure

(Add information about your project structure here)

## API Documentation

(Add information about your API endpoints here)

## Contributing

(Add guidelines for contributing to your project)

## License

(Add your license information here)
