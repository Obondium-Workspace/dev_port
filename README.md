# Dev_Port

## Overview

**Dev_Port** is a Content Management System (CMS) designed to manage and showcase portfolios. The project starts by focusing on portfolio management, using a customized Bootstrap template and integrating a Django-based dashboard for effective administration.

## Features

- **Portfolio Management**: Create, update, and manage portfolio entries.
- **Custom Bootstrap Template**: A responsive, customizable design to showcase portfolios.
- **Django Dashboard**: An administrative interface built with Django for managing portfolios and site content.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/dev_port.git
   ```

2. **Navigate into the project directory:**

   ```bash
   cd dev_port
   ```

3. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   Access the project at `http://127.0.0.1:8000/`.

## Project Structure

- **`main/`**: Contains the main application for managing portfolios.
- **`templates/`**: Contains HTML templates.
- **`static/`**: Contains static files like CSS, JavaScript, and images.
- **`media/`**: Directory for user-uploaded files.
- **`requirements.txt`**: Lists Python dependencies.
- **`manage.py`**: Django's command-line utility for administrative tasks.

## Contributing

This project is developed by the Obondium Workspace team. Contributions to enhance features or improve the codebase are welcome. Please refer to the guidelines in the `CONTRIBUTING.md` file for detailed instructions on how to contribute.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or support, please contact obondiumworkspace@gmail.com or create an issue on the [GitHub repository](https://github.com/yourusername/dev_port).


<hr>
<br>


```Copyright (c) Obondium. All rights reserved.```