# ReconCam - PehchanKaun

![ReconCam Logo](logo.jpg)

## Tagline
*PehchanKaun* - Recognizing faces, one at a time.

## Project Overview

*ReconCam* is a face recognition system built using the open-source InsightFace library. The system is designed to accurately identify faces, initially focusing on student recognition, with future applications in surveillance and reconnaissance.

The project is backed by RedisDB for in-memory caching, allowing for fast and efficient data processing. ReconCam is hosted on an AWS VM, though we are working on integrating a custom domain and applying SSL/TSL certificates for enhanced security. The user interface is developed using the Streamlit Python library, offering a smooth and intuitive experience.

## Features

- *Accurate Face Recognition*: Utilizing InsightFace, ReconCam ensures high-precision recognition in real-time.
- *In-Memory Caching*: Powered by RedisDB for quick data access and processing.
- *Scalable Infrastructure*: Deployed on AWS, with future plans for full domain integration and SSL/TSL support.
- *Easy-to-Use Interface*: Streamlit-based frontend provides a seamless user experience.
- *Versatile Applications*: While the primary focus is student recognition, the system can be adapted for surveillance and recon work.

## Tech Stack

- *Backend*: Python, InsightFace
- *Frontend*: Streamlit
- *Database*: RedisDB
- *Deployment*: AWS Virtual Machine
- *Future Integration*: Custom domain with SSL/TSL certificates

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.7+
- RedisDB
- Streamlit

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/reconcam.git
   cd reconcam
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Ensure RedisDB is installed and running. You can use the following commands to start Redis:

bash
Copy code
redis-server
Running the Application
To start the ReconCam application, run the following command:

bash
Copy code
streamlit run app.py
Deployment
The project is currently deployed on an AWS VM. To replicate the deployment:

Set up an AWS EC2 instance.
Install the required dependencies on the instance.
Run the application using the Streamlit command provided above.
Work is ongoing to integrate a custom domain and add SSL/TSL certification for secure communication.
Roadmap
 Student face recognition system
 Surveillance and reconnaissance use cases
 Full domain integration with SSL/TSL
 Enhanced analytics and reporting for users
Contributing
We welcome contributions! Please follow the steps below to contribute to ReconCam:

Fork the repository.
Create a new branch for your feature: git checkout -b feature-name.
Commit your changes: git commit -m 'Add feature'.
Push to the branch: git push origin feature-name.
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
InsightFace for their open-source library.
RedisDB for providing fast in-memory caching.
AWS for cloud infrastructure support.
Streamlit for making web development easy with Python.
Feel free to fork the project, explore the code, and contribute! If you have any questions or run into issues, feel free to reach out to us via issues or pull requests.

markdown
Copy code

### Key Sections Explained:

- *Project Overview* gives a brief description of ReconCam and its purpose.
- **Features
