from flask import Flask, render_template, jsonify
import speedtest
import threading
import time
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# List to store the latest 10 internet speed statistics
speed_stats = []

def measure_speed():
    while True:
        try:
            st = speedtest.Speedtest()
            st.download()
            st.upload()
            result = st.results.dict()
            
            # Store only the required fields: download, upload, ping
            speed_stats.append({
                'download': result['download'] / 1e6,  # Convert to Mbps
                'upload': result['upload'] / 1e6,  # Convert to Mbps
                'ping': result['ping']
            })
            
            # Keep only the latest 10 statistics
            if len(speed_stats) > 10:
                speed_stats.pop(0)
        
        except Exception as e:
            print(f"Error measuring speed: {e}")
        
        # Wait for 5 seconds before measuring again
        time.sleep(5)

# Start the speed measurement in a separate thread
threading.Thread(target=measure_speed, daemon=True).start()

@app.route('/')
def index():
    return render_template('flaskspeedtest.html', speed_stats=speed_stats)

@app.route('/speed_stats')
def get_speed_stats():
    return jsonify(speed_stats)

@app.route('/plot')
def plot():
    # Generate the plot only when this route is accessed
    download_speeds = [stat['download'] for stat in speed_stats]
    upload_speeds = [stat['upload'] for stat in speed_stats]
    pings = [stat['ping'] for stat in speed_stats]

    fig, ax = plt.subplots(3, 1, figsize=(10, 15))
    
    ax[0].plot(download_speeds, marker='o')
    ax[0].set_title('Download Speed (Mbps)')
    ax[0].set_ylabel('Mbps')
    
    ax[1].plot(upload_speeds, marker='o')
    ax[1].set_title('Upload Speed (Mbps)')
    ax[1].set_ylabel('Mbps')
    
    ax[2].plot(pings, marker='o')
    ax[2].set_title('Ping (ms)')
    ax[2].set_ylabel('ms')
    
    plt.tight_layout()
    
    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    plt.close(fig)  # Close the plot to free resources

    return f'<img src="data:image/png;base64,{plot_url}"/>'

if __name__ == '__main__':
    app.run(debug=True)
