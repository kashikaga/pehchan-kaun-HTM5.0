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

## Installation of Dependencies

1. **Install Required Packages**  
   Use the following command to install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Ensure RedisDB is Installed and Running**  
   Start RedisDB using the command:
   ```bash
   redis-server
   ```

## Running the Application

To start the ReconCam application, execute:
```bash
streamlit run app.py
```

## Deployment Instructions

The project is currently deployed on an AWS VM. To replicate the deployment:

1. Set up an **AWS EC2 instance**.
2. Install the required dependencies on the instance.
3. Run the application using the Streamlit command provided above.

**Note:** Work is ongoing to integrate a custom domain and add SSL/TLS certification for secure communication.

## Roadmap

- **Student face recognition system**
- **Surveillance and reconnaissance use cases**
- **Full domain integration with SSL/TLS**
- **Enhanced analytics and reporting for users**

## Contributing

We welcome contributions! Please follow these steps to contribute to ReconCam:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **InsightFace** for their open-source library.
- **RedisDB** for providing fast in-memory caching.
- **AWS** for cloud infrastructure support.
- **Streamlit** for making web development easy with Python.

Feel free to fork the project, explore the code, and contribute! If you have any questions or run into issues, reach out via issues or pull requests.



