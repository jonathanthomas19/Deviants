
# Velocity Kingdom Project
This project is a Virtual Reality exploration focused on different types of racing: Formula Racing, Rally Racing, and Street Racing. It uses web technologies to create immersive experiences.

## Project Structure
- `frontend/index.html`: Entry point for the VR experience.
- `frontend/assets/models`: Directory for 3D models of racing cars.
- `frontend/js/`: JavaScript logic for the VR experience.
- `frontend/css/`: Styles for the web experience.

## FastAPI Setup
The project includes a FastAPI application for serving the VR experience and handling API requests.

### Running the Server
1. Ensure dependencies are installed:
   ```shell
   pip install fastapi uvicorn
   ```
2. Start the server with:
   ```shell
   uvicorn main:app --reload
   ```
3. Access the application at `http://127.0.0.1:8000`. Static files are served under `/static`.

## Updating 3D Models
Replace the placeholder models in `frontend/assets/models` with actual 3D models of racing cars. Be sure to check the models' licenses and provide attribution as required.
