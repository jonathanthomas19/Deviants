
# Velocity Kingdom Project

This project is a Virtual Reality exploration focused on different types of racing: Formula Racing, Rally Racing, and Street Racing. It uses web technologies to create immersive experiences.

## Project Structure
- `frontend/index.html`: Entry point for the VR experience.
- `frontend/assets/models`: Directory for 3D models of racing cars.
- `frontend/js/`: JavaScript logic for the VR experience.
- `frontend/css/`: Styles for the web experience.

## FastAPI Setup
This project uses FastAPI as its backend to serve static files and handle API requests.
- Ensure you have FastAPI installed. If not, you can install it using pip:
  ```
  pip install fastapi[all]
  ```
- To run the backend, navigate to the project directory and execute:
  ```
  uvicorn main:app --reload
  ```
  This command will start the FastAPI server, making the backend accessible on `http://localhost:8000`. The `--reload` flag enables automatic reloading during development.

## Running the Project Locally
1. Start the FastAPI backend as described in the FastAPI Setup section.
2. Access the VR experience by navigating to `http://localhost:8000/` in your web browser. The backend serves the frontend directly from the root URL.

## Dependencies
- FastAPI: For the backend server and API.
- Uvicorn: As an ASGI server to run FastAPI.
  You can install these dependencies using:
  ```
  pip install fastapi[all] uvicorn
  ```

## Additional Notes
- The `main.py` file contains the backend logic for serving the `index.html` as the default page and handling the root API endpoint.
- Explore the `frontend` directory for web assets and VR experience logic.
