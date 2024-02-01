# Python Script Toolbox

A collection of versatile Python scripts designed to serve as a toolbox for various tasks, with a focus on aiding in cybersecurity, ethical hacking automation, and bug bounty initiatives. From simple utilities to more complex functionalities, this repository aims to provide a range of tools that can be easily integrated into different projects.

## Features:
**1.** **Network Scanner (`network_scanner.py`):** A script designed for scanning networks, identifying active hosts, and providing essential information about each device. Useful for cybersecurity assessments and network monitoring.

  - **Usage:**
    - Ensure you have Python installed.
    - Open a terminal and navigate to the directory containing `network_scanner.py`.
    - Run the following command:
      ```bash
      python network_scanner.py
      ```
    - Follow the prompts to enter the target IP address, starting port, and ending port.

  - **Dependencies:**
    - This script requires Python. You can download it from [python.org](https://www.python.org/downloads/).
    - No additional Python packages are needed.

  - **Notes:**
    - Adjust the timeout in `sock.settimeout(1)` if needed for your network conditions.
    - Please use this tool responsibly and in accordance with applicable laws and regulations.

**2.** **Password Manager (`password_manager.py`):** Securely manage your passwords with our Python-based Password Manager. This tool provides a simple yet effective way to store and retrieve passwords for different accounts and categories.

- **Secure Encryption:** Utilizes the `cryptography` library for robust encryption, ensuring the confidentiality of stored passwords.

- **User-Friendly Interface:** Easy-to-use command-line interface for adding and retrieving passwords.

- **Data Persistence:** Passwords are encrypted and stored persistently, allowing users to access their passwords across sessions.

 - **Usage:**

   - **Installation:**
     - Clone the repository: `git clone https://github.com/binbash0/python-script-toolbox.git`
     - Navigate to the project directory: `cd python-script-toolbox`

   - **Run the Password Manager:**
     - Execute the script: `python password_manager.py`
     - Follow the prompts to add or retrieve passwords.

   - **Master Password:**
     - You will be prompted to enter a master password when running the Password Manager. This password is used for encryption and decryption.

- **Example:**

```bash
# Add a password
python password_manager.py

# Retrieve a password
python password_manager.py
```

- **Dependencies:**
- [`cryptography`](https://cryptography.io/en/latest/)

- **Note:**
Please ensure that you have Python and the required dependencies installed before using the Password Manager.



## Usage:

Explore the scripts and find tools that suit your needs, especially in the realms of cybersecurity, ethical hacking, and bug bounty programs. Each script is designed for modularity and ease of integration. Refer to individual script directories for specific usage instructions.

## Contributions:

Feel free to contribute your own scripts or improvements. Open to collaboration and making this Python Script Toolbox a comprehensive resource for developers in the cybersecurity community.

## Disclaimer:

The scripts provided in this repository are for educational and ethical purposes only. Users are responsible for compliance with applicable laws and regulations. The maintainers disclaim any liability for misuse or unauthorized activities.

## License:

This project is licensed under the [MIT License](LICENSE).
