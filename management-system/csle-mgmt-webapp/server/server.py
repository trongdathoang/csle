import csle_rest_api.rest_api as rest_api
import os

if __name__ == '__main__':
    try:
        # Use absolute path to the build directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        static_folder_path = os.path.abspath(os.path.join(current_dir, "../build"))
        
        print(f"Using static folder path: {static_folder_path}")
        
        # Start the full REST API server with the React frontend
        rest_api.start_server(
            static_folder=static_folder_path,
            port=7777,
            num_threads=100,
            host="0.0.0.0",
            https=False
        )
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        print(traceback.format_exc())
